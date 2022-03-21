from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=32)
    armorType = models.CharField(max_length=10, blank=True, default='')
    armorBonus = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    shieldBonus = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    ACP = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    ASF = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    maxDex = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    weaponType = models.CharField(max_length=10, blank=True, null=True, default='')
    weaponUsage = models.CharField(max_length=10, blank=True, null=True, default='')
    mediumDamage = models.CharField(max_length=10, blank=True, null=True, default='')
    mediumWeight = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    finesse = models.BooleanField(blank=True, null=True, default=False)
    reach = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    range = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    damageType = models.CharField(max_length=10, blank=True, null=True, default='')
    special = models.TextField(blank=True, null=True, default='')