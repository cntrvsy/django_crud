from django.db import models

# Create your models here.

class TodoItems(models.Model):
    item = models.CharField(max_length=200)
    done = models.BooleanField(default=False)