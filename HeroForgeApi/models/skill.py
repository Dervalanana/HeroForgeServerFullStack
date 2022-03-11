from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=55)
    trainedOnly = models.BooleanField()
    multiType = models.BooleanField()
    attribute = models.CharField(length=3)