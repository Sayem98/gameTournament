from django.db import models
from login_site.models import UserModel


# Create your models here.

class TournamentsModel(models.Model):
    game_type = models.CharField(max_length=20)
    tournament_name = models.CharField(max_length=30)
    your_email = models.EmailField(default='sa@gmail.com')
    fee = models.CharField(max_length=5)
    team_numbers = models.CharField(max_length=2)
    creator_name = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='creator', default=None)

    def __str__(self):
        return f'{self.game_type} {self.tournament_name} by {self.your_email}'


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
