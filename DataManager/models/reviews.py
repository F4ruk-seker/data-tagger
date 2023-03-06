from django.db import models
from autoslug import AutoSlugField


class Reviews(models.Model):
    name = models.TextField(null=True)
    slug = AutoSlugField(populate_from='name')
    explanation = models.TextField(null=True)
    comments = models.ManyToManyField('DataManager.Comment',blank=True)

    def get_comments(self):
        return self.comments.all()

    def get_comment_count(self):
        return self.comments.count()

    def __str__(self):
        return str(self.name)

