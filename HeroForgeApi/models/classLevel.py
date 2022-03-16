
from django.db import models


class ClassLevel(models.Model):
    classId = models.ForeignKey("Classs", on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField()
    features = models.TextField()
    fixedFeat = models.ForeignKey("Feat", on_delete=models.SET_NULL, null=True, blank=True)
    featSetId = models.ForeignKey("FeatSet", on_delete=models.SET_NULL, null=True, blank=True)
    BAB = models.PositiveSmallIntegerField()
    Fort = models.PositiveSmallIntegerField()
    Ref = models.PositiveSmallIntegerField()
    Will = models.PositiveSmallIntegerField()