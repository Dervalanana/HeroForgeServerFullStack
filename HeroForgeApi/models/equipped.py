from django.db import models


class Equipped(models.Model):
    equipmentId= models.ForeignKey("Equipment", on_delete=models.CASCADE)
    characterId= models.ForeignKey("Character", on_delete=models.CASCADE)