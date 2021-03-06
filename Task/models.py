from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Subtask(models.Model):
    title = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.title