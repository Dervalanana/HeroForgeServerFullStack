
from django.db import models


class ClassLevel(models.Model):
    classs = models.ForeignKey("Classs", on_delete=models.CASCADE, related_name="levelDetails")
    level = models.PositiveSmallIntegerField()
    features = models.TextField()
    fixedFeat = models.ForeignKey("Feat", on_delete=models.SET_NULL, null=True, blank=True)
    featSet = models.ForeignKey("FeatSet", on_delete=models.SET_NULL, null=True, blank=True)
    BAB = models.PositiveSmallIntegerField()
    Fort = models.PositiveSmallIntegerField()
    Ref = models.PositiveSmallIntegerField()
    Will = models.PositiveSmallIntegerField()