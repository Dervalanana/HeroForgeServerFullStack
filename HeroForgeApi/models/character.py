from django.db import models
from HeroForgeApi.models import Race
from django.contrib.auth.models import User
from HeroForgeApi.models import equipment
from HeroForgeApi.models.equipment import Equipment
from HeroForgeApi.models.equipped import Equipped
from HeroForgeApi.models.proficiencies import Proficiency


class Character(models.Model):
    xp = models.SmallIntegerField(default=0)
    name = models.CharField(max_length=64)
    campaign = models.CharField(max_length=64, blank=True, null=True)
    str = models.SmallIntegerField(default=0)
    dex = models.SmallIntegerField(default=0)
    con = models.SmallIntegerField(default=0)
    int = models.SmallIntegerField(default=0)
    wis = models.SmallIntegerField(default=0)
    cha = models.SmallIntegerField(default=0)
    raceId = models.ForeignKey(Race, on_delete=models.SET_DEFAULT, default=1)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    proficiencies = models.ManyToManyField(Equipment, through="Proficiency", related_name="Proficiencies")
    equipment = models.ManyToManyField(Equipment, through="Equipped")