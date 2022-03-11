from statistics import mode
from django.db import models

from HeroForgeApi.models.feat import Feat
from HeroForgeApi.models import FeatOption

class FeatSet(models.model):
    name= models.CharField()
    featOptions = models.ManyToManyField(Feat, through=FeatOption)