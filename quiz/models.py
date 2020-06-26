from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length = 255)
    answer = models.CharField(max_length = 255)
    hint = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Badge(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Player(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    badge = models.ForeignKey(Badge, on_delete = models.CASCADE, blank=False, null=True)
    totalPts = models.IntegerField(default=0)
    totalQuestionsCreated = models.IntegerField(default = 0)

    def __str__(self):
        return self.firstname + " " + self.lastname 

    
class Statistics(models.Model):
    profile = models.ForeignKey(Player, on_delete = models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    numberTrue = models.IntegerField()
    numberFalse = models.IntegerField()

    def __str__(self):
        return self.profile.username + ' - true: ' + str(self.numberTrue) + ', false: ' + str(self.numberFalse) + 'answers'

