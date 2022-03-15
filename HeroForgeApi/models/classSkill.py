
from django.db import models

class ClassSkill(models.Model):
    value = models.BooleanField()
    classId = models.ForeignKey("Classs", on_delete=models.CASCADE)
    skillId = models.ForeignKey("Skill", on_delete=models.CASCADE)