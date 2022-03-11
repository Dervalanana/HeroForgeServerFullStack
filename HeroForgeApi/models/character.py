from cgitb import small
from statistics import mode
from tkinter import CASCADE
from django.db import models

from HeroForgeApi.models import Race
from django.contrib.auth.models import User
from HeroForgeApi.models import equipment

from HeroForgeApi.models.equipment import Equipment
from HeroForgeApi.models.equipped import Equipped
from HeroForgeApi.models.proficiencies import Proficiency


class Character(models.model):
    xp = models.SmallIntegerField(default=0)
    name = models.CharField()
    campaign = models.CharField(blank=True, null=True)
    str = models.SmallIntegerField(default=0)
    dex = models.SmallIntegerField(default=0)
    con = models.SmallIntegerField(default=0)
    int = models.SmallIntegerField(default=0)
    wis = models.SmallIntegerField(default=0)
    cha = models.SmallIntegerField(default=0)
    raceId = models.ForeignKey(Race, on_delete=models.SET_DEFAULT, default=1)
    userId = models.ForeignKey(User, on_delete=CASCADE)
    proficiencies = models.ManyToManyField(Equipment, Proficiency)
    equipment = models.ManyToManyField(Equipment, Equipped)