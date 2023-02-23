from django.db import models

class Tag(models.Model):
    name = models.TextField(null=True)
    explanation = models.TextField(null=True,default=None)

    def __str__(self):
        return str(self.name)