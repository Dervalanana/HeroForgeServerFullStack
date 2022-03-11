from tkinter import CASCADE
from django.db import models
from HeroForgeApi.models.character import Character

from HeroForgeApi.models.equipment import Equipment

class Proficiency(models.model):
    source= models.CharField()
    sourceId = models.PositiveSmallIntegerField()
    equipmentId = models.ForeignKey(Equipment, on_delete=CASCADE)
    characterId = models.ForeignKey(Character, on_delete=CASCADE)