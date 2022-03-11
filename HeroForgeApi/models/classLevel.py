from tkinter import CASCADE
from django.db import models
from HeroForgeApi.models.feat import Feat
from HeroForgeApi.models.featSet import FeatSet
from models import Classs

class ClassLevel(models.model):
    classId = models.ForeignKey(Classs, on_delete=CASCADE)
    level = models.PositiveSmallIntegerField()
    features = models.TextField()
    fixedFeat = models.ForeignKey(Feat, on_delete=models.SET_NULL, null=True, blank=True)
    featSetId = models.ForeignKey(FeatSet, on_delete=models.SET_NULL, null=True, blank=True)
    BAB = models.PositiveSmallIntegerField()
    Fort = models.PositiveSmallIntegerField()
    Ref = models.PositiveSmallIntegerField()
    Will = models.PositiveSmallIntegerField()