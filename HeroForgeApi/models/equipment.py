from django.db import models

class Equipment(models.Model):
    name=models.CharField(max_length=32)
    armorType = models.CharField(max_length=10, blank=True)
    armorBonus = models.PositiveSmallIntegerField(blank=True, null=True)
    shieldBonus = models.PositiveSmallIntegerField(blank=True, null=True)
    ACP = models.PositiveSmallIntegerField(blank=True, null=True)
    ASF = models.PositiveSmallIntegerField(blank=True, null=True)
    maxDex = models.PositiveSmallIntegerField(blank=True, null=True)
    weaponType = models.CharField(max_length=10, blank=True, null=True)
    weaponUsage = models.CharField(max_length=10, blank=True, null=True)
    mediumDamage = models.CharField(max_length=10, blank=True, null=True)
    mediumWeight = models.PositiveSmallIntegerField(blank=True, null=True)
    finesse = models.BooleanField(blank=True, null=True)
    reach = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveSmallIntegerField(blank=True, null=True)
    damageType = models.CharField(max_length=10, blank=True, null=True)
    special = models.TextField(blank=True, null=True)