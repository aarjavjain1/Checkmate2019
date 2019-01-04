from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
class Team(models.Model):
    score = models.IntegerField(blank=True)
    team_name = models.CharField(max_length=250, unique=True)
    #team_desc = models.CharField(max_length=250, blank=True)
    #number_of_players = models.IntegerField(validators=[MaxValueValidator(2)])

    def __str__(self):
        return self.team_name


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='team', on_delete=models.CASCADE, blank=True)
