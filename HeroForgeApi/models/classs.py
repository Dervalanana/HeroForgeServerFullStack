from django.db import models

from HeroForgeApi.models import classSkill
from HeroForgeApi.models import Skill, ClassSkill

class Classs(models.Model):
    name = models.CharField(max_length=55)
    skillPoints = models.CharField()
    HD = models.CharField()
    classSkills = models.ManyToManyField(Skill, ClassSkill)