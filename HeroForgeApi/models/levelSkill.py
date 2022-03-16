from django.db import models

class LevelSkill(models.Model):
    levelId = models.ForeignKey("Level", on_delete=models.CASCADE)
    skillId = models.ForeignKey("Skill", on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(default = 0)
    multiTypeName = models.CharField(max_length=3, blank=True)
    