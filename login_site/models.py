from django.db import models


# Create your models here.

class UserModel(models.Model):
    your_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    user_image = models.ImageField(upload_to='image')
    pubgID = models.CharField(max_length=20, blank=True)
    Sea_of_theves_id = models.CharField(max_length=20, blank=True)
    Call_of_duty_id = models.CharField(max_length=20, blank=True)

    phone = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return f'{self.your_name} {self.email}'
