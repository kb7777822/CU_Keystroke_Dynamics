from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

#class Board(models.Model):


class SnakeItem(models.Model):
    color = models.CharField(max_length=20)
    squares = ArrayField(models.IntegerField(default=-1))
    direction = models.CharField(max_length=1)

    def __str__(self):
        return self.color
