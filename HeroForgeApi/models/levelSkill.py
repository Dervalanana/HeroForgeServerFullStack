from tkinter import CASCADE
from django.db import models

from HeroForgeApi.models.level import Level
from HeroForgeApi.models.skill import Skill

class LevelSkills(models.model):
    levelId = models.ForeignKey(Level, on_delete=CASCADE)
    skillId = models.ForeignKey(Skill, on_delete=CASCADE)
    points = models.PositiveSmallIntegerField(default = 0)
    multiTypeName = models.CharField(blank=True)
    