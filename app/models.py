from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices = [
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Not Completed', 'Not Completed')
    ])