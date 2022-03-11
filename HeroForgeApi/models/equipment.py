from django.db import models

class Equipment(models.model):
    name=models.CharField()
    armorType = models.CharField(blank=True)
    armorBonus = models.PositiveSmallIntegerField(blank=True, null=True)
    shieldBonus = models.PositiveSmallIntegerField(blank=True, null=True)
    ACP = models.PositiveSmallIntegerField(blank=True, null=True)
    ASF = models.PositiveSmallIntegerField(blank=True, null=True)
    maxDex = models.PositiveSmallIntegerField(blank=True, null=True)
    weaponType = models.CharField(blank=True, null=True)
    weaponUsage = models.CharField(blank=True, null=True)
    mediumDamage = models.CharField(blank=True, null=True)
    mediumWeight = models.CharField(blank=True, null=True)
    finesse = models.BooleanField(blank=True, null=True)
    reach = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveSmallIntegerField(blank=True, null=True)
    damageType = models.CharField(blank=True, null=True)
    special = models.TextField(blank=True, null=True)