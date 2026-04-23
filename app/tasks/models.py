from django.db import models
import os

class Task(models.Model):
    title = models.CharField(max_length=200)
    assignee = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='시작전')
    deadline = models.DateField()
    priority = models.IntegerField(default=1)
    memo = models.TextField(blank=True)

    def delete(self, *args, **kwargs):
        for f in self.files.all():
            if f.file and os.path.isfile(f.file.path):
                os.remove(f.file.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class TaskFile(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='files'
    )
    file = models.FileField(upload_to='uploads/')

    def delete(self, *args, **kwargs):
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.file.name
