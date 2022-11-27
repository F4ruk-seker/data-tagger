from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.TextField(null=True)
    def __str__(self):
        return str(self.name)