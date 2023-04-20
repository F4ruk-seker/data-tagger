from django.db import models
from autoslug import AutoSlugField

from .tags import Tag


class Reviews(models.Model):
    name = models.TextField(null=True)
    slug = AutoSlugField(populate_from='name')
    explanation = models.TextField(null=True)
    comments = models.ManyToManyField('DataManager.Comment',blank=True)

    def get_comments(self):
        return self.comments.all()

    def get_comment_count(self):
        return self.comments.count()

    def get_stats(self):
        tag_list = Tag.objects.all()
        tag_list_dict = {}

        for tag in tag_list:
            tag_list_dict[tag.name] = 0

        for tag in tag_list:
            tag_list_dict[tag.name] = self.comments.filter(tag=tag).count()

        tag_list_dict["unTAG"] = self.comments.filter(tag=None).count()

        return tag_list_dict




    def __str__(self):
        return str(self.name)

