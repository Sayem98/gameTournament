from django.db import models


# Create your models here.

class TournamentsModel(models.Model):
    game_type = models.CharField(max_length=20)
    tournament_name = models.CharField(max_length=30)
    your_email = models.EmailField()
    fee = models.CharField(max_length=5)
    team_numbers = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.game_type} {self.tournament_name} by {self.your_email}'
