from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="Technical")
    proficiency = models.IntegerField(default=80, help_text="Proficiency percentage from 1 to 100")

    def __str__(self):
        return self.name
