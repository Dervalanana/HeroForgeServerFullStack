from django.db import models
from HeroForgeApi.models import Skill

class Level(models.Model):
    characterId = models.ForeignKey("Character", on_delete=models.CASCADE)
    classId = models.ForeignKey("Classs", on_delete=models.SET_DEFAULT, default=1)
    characterLevel = models.PositiveSmallIntegerField()
    HDRoll = models.PositiveSmallIntegerField(default=0)
    statIncrease = models.CharField(max_length=3, blank=True, null=True)
    featId = models.ForeignKey("Feat",on_delete=models.SET_DEFAULT, default=0, blank=True, null=True)
    levelSkills = models.ManyToManyField(Skill, through="LevelSkill")