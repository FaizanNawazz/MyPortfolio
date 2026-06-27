from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=255, help_text="URL or static file path to profile picture")
    description = models.TextField()

    def __str__(self):
        return self.name
