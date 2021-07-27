import datetime

from django.db import models
from login_site.models import UserModel
from django.utils.text import slugify
import string
import random
from datetime import date
from django.utils import timezone


# Create your helper functions here.
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


# Create your models here.

class TournamentsModel(models.Model):
    game_type = models.CharField(max_length=20)
    tournament_name = models.CharField(max_length=30)
    your_email = models.EmailField(default='sa@gmail.com')
    fee = models.CharField(max_length=5)
    team_numbers = models.CharField(max_length=2)
    creator_name = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='creator', default=None)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_register_date = models.DateField()

    def __str__(self):
        return f'{self.game_type} {self.tournament_name} by {self.your_email} at {self.creation_date}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + '-' + self.tournament_name)
            print(self.slug)
        super(TournamentsModel, self).save(*args, **kwargs)


class TeamsModel(models.Model):
    team_name = models.CharField(max_length=20, default='My Team')
    player1 = models.CharField(max_length=10)

    player2 = models.CharField(max_length=10)
    player3 = models.CharField(max_length=10)
    player4 = models.CharField(max_length=10)
    leader = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='player1', default=None)
    # leader = models.CharField(max_length=10)
    tournament = models.ForeignKey(TournamentsModel, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return f'{self.team_name}'
