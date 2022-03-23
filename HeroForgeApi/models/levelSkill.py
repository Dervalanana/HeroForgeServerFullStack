from django.db import models

class LevelSkill(models.Model):
    level = models.ForeignKey("Level", on_delete=models.CASCADE, related_name="skillAssignment")
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(default = 0)
    multiTypeName = models.CharField(max_length=3, blank=True)
    