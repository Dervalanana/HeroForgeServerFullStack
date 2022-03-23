from django.db import models


class Feat(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=511)
    strPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    dexPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    conPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    intPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    wisPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    chaPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    fortPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    refPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    willPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    babPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    classLevelPR= models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    classPR= models.ForeignKey("Classs", models.SET_NULL, blank=True, null=True, default=None)
    feat1PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, default=None, related_name='+')
    feat2PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, default=None, related_name='+')
    feat3PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, default=None, related_name='+')
    feat4PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, default=None, related_name='+')