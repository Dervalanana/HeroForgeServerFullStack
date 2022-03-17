from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=55)
    trainedOnly = models.BooleanField(default=False)
    multiType = models.SmallIntegerField()
    attribute = models.CharField(max_length=3)