from pyexpat import model
from django.db import models


class Equipped(models.Model):
    equipment= models.ForeignKey("Equipment", on_delete=models.CASCADE)
    character= models.ForeignKey("Character", on_delete=models.CASCADE, related_name="equipment")
    slot = models.PositiveSmallIntegerField(blank=True, null=True)