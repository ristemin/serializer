from django.db import models

class Task(models.Model):
    title = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title