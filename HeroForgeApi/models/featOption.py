from django.db import models


class FeatOption(models.Model):
    feat = models.ForeignKey("Feat", on_delete=models.CASCADE)
    featSet = models.ForeignKey("FeatSet", on_delete=models.CASCADE)