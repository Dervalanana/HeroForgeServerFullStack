from tkinter import CASCADE
from django.db import models
from models import Classs, Skill

class ClassSkill(models.model):
    value = models.BooleanField()
    classId = models.ForeignKey(Classs, on_delete=CASCADE)
    skillId = models.ForeignKey(Skill, on_delete=CASCADE)