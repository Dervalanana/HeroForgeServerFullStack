from tkinter import CASCADE
from django.db import models

from HeroForgeApi.models import Feat, FeatSet

class FeatOption(models.model):
    featId = models.ForeignKey(Feat, on_delete=CASCADE)
    featSetId = models.ForeignKey(FeatSet, on_delete=CASCADE)