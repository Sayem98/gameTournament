from django.db import models


# Create your models here.

class UserModel(models.Model):
    your_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.your_name} {self.email}'
