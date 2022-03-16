from django.db import models

class Proficiency(models.Model):
    source= models.CharField(max_length=10)
    sourceId = models.PositiveSmallIntegerField()
    equipmentId = models.ForeignKey("Equipment", on_delete=models.CASCADE)
    characterId = models.ForeignKey("Character", on_delete=models.CASCADE)