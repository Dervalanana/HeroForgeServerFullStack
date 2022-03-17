from django.db import models

class CharacterFeat(models.Model):
    feat = models.ForeignKey("Feat", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    specificOption = models.PositiveSmallIntegerField(blank=True, null=True)
    optionSource = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    sourceId = models.PositiveSmallIntegerField()
    