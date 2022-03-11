from django.db import models
from models import Feat, FeatSet

class Race(models.Model):
    name = models.CharField(max_length=55)
    racialBonus = models.CharField(max_length=55, blank=True)
    racialPenalty = models.CharField(max_length=55, blank=True)
    special = models.CharField(max_length=55, blank=True)
    speed = models.CharField(max_length=55)
    altSpeedType = models.CharField(max_length=55, blank=True)
    altSpeed = models.PositiveSmallIntegerField(blank=True, null=True)
    featId = models.ForeignKey(Feat, models.SET_NULL, blank=True, null=True)
    featSetId = models.ForeignKey(FeatSet, models.SET_NULL, blank=True, null=True)