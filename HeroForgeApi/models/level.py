from django.db import models
from HeroForgeApi.models import Skill

class Level(models.Model):
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    classs = models.ForeignKey("Classs", on_delete=models.SET_DEFAULT, default=1)
    characterLevel = models.PositiveSmallIntegerField()
    HDRoll = models.PositiveSmallIntegerField(default=0)
    statIncrease = models.CharField(max_length=3, blank=True, null=True)
    feat = models.ForeignKey("Feat",on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, related_name='+')
    levelSkills = models.ManyToManyField(Skill, through="LevelSkill")
    classFeat = models.ForeignKey("Feat", on_delete=models.SET_DEFAULT, blank=True, null=True, default=None, related_name='+')
    levelDetails = models.ForeignKey("ClassLevel", on_delete=models.SET_NULL, blank=True, null=True, default=None, related_name='+')