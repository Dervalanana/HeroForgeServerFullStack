from django.db import models


class Equipped(models.Model):
    equipment= models.ForeignKey("Equipment", on_delete=models.CASCADE)
    character= models.ForeignKey("Character", on_delete=models.CASCADE)