from operator import mod
from django.db import models

# Create your models here.
class Text(models.Model):
    words = models.TextField()

    def __str__(self):
        return f"{self.words}"

