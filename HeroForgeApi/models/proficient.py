from django.db import models

class Proficient(models.Model):
    classLevel = models.ForeignKey("ClassLevel", on_delete=models.CASCADE, default=None, blank=True, null=True)
    race = models.ForeignKey("Race", on_delete=models.CASCADE, default=None, blank=True, null=True)
    equipment = models.ForeignKey("Equipment", on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    