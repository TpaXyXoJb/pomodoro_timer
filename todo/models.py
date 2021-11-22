from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])


class Loop(models.Model):
    duration = models.CharField(max_length=16)
    timeout = models.CharField(max_length=16)
    rounds = models.CharField(max_length=16)
    is_started = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    tasks = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('loop_detail', args=[str(self.id)])

