from tkinter import CASCADE
from django.db import models

from HeroForgeApi.models.character import Character
from HeroForgeApi.models.classs import Classs
from HeroForgeApi.models.feat import Feat
from HeroForgeApi.models import Skill, LevelSkills


class Level(models.model):
    characterId = models.ForeignKey(Character, on_delete=CASCADE)
    classId = models.ForeignKey(Classs, on_delete=models.SET_DEFAULT, default=1)
    characterLevel = models.PositiveSmallIntegerField()
    HDRoll = models.PositiveSmallIntegerField(default=0)
    statIncrease = models.CharField(max_length=3, blank=True, null=True)
    featId = models.ForeignKey(Feat,on_delete=models.SET_DEFAULT, default=0, blank=True, null=True)
    levelSkills = models.ManyToManyField(Skill, LevelSkills)