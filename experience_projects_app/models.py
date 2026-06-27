from django.db import models

class ProjectExperience(models.Model):
    TYPE_CHOICES = [
        ('project', 'Personal Project'),
        ('experience', 'Professional Experience'),
        ('academic', 'Academic Project'),
    ]
    
    title = models.CharField(max_length=200)
    item_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='project')
    description = models.TextField()
    technologies = models.CharField(max_length=200, help_text="Comma-separated technologies used")
    duration = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True, help_text="Link to github repo or demo")

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.technologies.split(',')]
