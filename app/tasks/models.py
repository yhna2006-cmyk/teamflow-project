from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assignee = models.CharField(max_length=50)
    deadline = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.title
