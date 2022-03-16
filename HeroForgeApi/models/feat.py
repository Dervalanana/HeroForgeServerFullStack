from django.db import models


class Feat(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=511)
    strPR= models.PositiveSmallIntegerField(blank=True, null=True)
    dexPR= models.PositiveSmallIntegerField(blank=True, null=True)
    conPR= models.PositiveSmallIntegerField(blank=True, null=True)
    intPR= models.PositiveSmallIntegerField(blank=True, null=True)
    wisPR= models.PositiveSmallIntegerField(blank=True, null=True)
    chaPR= models.PositiveSmallIntegerField(blank=True, null=True)
    fortPR= models.PositiveSmallIntegerField(blank=True, null=True)
    refPR= models.PositiveSmallIntegerField(blank=True, null=True)
    willPR= models.PositiveSmallIntegerField(blank=True, null=True)
    babPR= models.PositiveSmallIntegerField(blank=True, null=True)
    classLevelPR= models.PositiveSmallIntegerField(blank=True, null=True)
    classPR= models.ForeignKey("Classs", models.SET_NULL, blank=True, null=True)
    feat1PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, related_name='+')
    feat2PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, related_name='+')
    feat3PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, related_name='+')
    feat4PR= models.ForeignKey('self', models.SET_NULL, blank=True, null=True, related_name='+')