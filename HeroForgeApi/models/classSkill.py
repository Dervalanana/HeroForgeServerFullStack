
from django.db import models

class ClassSkill(models.Model):
    value = models.BooleanField()
    classs = models.ForeignKey("Classs", on_delete=models.CASCADE)
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE)