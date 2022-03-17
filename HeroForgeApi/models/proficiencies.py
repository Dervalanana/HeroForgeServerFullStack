from django.db import models

class Proficiency(models.Model):
    source= models.CharField(max_length=10)
    sourceId = models.PositiveSmallIntegerField()
    equipment = models.ForeignKey("Equipment", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)