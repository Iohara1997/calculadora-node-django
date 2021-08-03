from django.db import models

class Post(models.Model):
    firstNumber = models.IntegerField()
    secondNumber = models.IntegerField()

