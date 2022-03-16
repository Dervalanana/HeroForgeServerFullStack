from statistics import mode
from django.db import models

from HeroForgeApi.models.feat import Feat
from HeroForgeApi.models import FeatOption

class FeatSet(models.Model):
    name= models.CharField(max_length=32)
    featOptions = models.ManyToManyField(Feat, through="FeatOption")