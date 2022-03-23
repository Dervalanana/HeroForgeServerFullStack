
from django.db import models

class ClassSkill(models.Model):
    value = models.BooleanField()
    classs = models.ForeignKey("Classs", on_delete=models.CASCADE, related_name="skillProficiency")
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE)