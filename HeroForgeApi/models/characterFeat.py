from django.db import models

class CharacterFeat(models.Model):
    featId = models.ForeignKey("Feat", on_delete=models.CASCADE)
    characterId = models.ForeignKey("Character", on_delete=models.CASCADE)
    specificOption = models.PositiveSmallIntegerField(blank=True, null=True)
    optionSource = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    sourceId = models.PositiveSmallIntegerField()
    