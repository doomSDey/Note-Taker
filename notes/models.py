# Create your models here.
from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=120)
    title = models.CharField(max_length=120,default="Note")
    color = models.CharField(max_length=120,default="yellow")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
