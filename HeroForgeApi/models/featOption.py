from django.db import models


class FeatOption(models.Model):
    featId = models.ForeignKey("Feat", on_delete=models.CASCADE)
    featSetId = models.ForeignKey("FeatSet", on_delete=models.CASCADE)