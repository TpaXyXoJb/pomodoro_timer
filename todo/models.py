from django.contrib.auth.models import User
from django.db import models


class TaskList(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Loop(models.Model):
    is_finished = models.BooleanField(default=False)
    finished_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(TaskList)
