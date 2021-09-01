from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField(max_length=1000)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
