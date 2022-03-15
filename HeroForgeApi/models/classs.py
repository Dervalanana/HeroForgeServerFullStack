from django.db import models
from HeroForgeApi.models.skill import Skill


class Classs(models.Model):
    name = models.CharField(max_length=55)
    skillPoints = models.PositiveSmallIntegerField()
    HD = models.PositiveSmallIntegerField()
    classSkills = models.ManyToManyField(Skill, through="ClassSkill")