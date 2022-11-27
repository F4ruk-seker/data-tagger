from django.db import models

class Comment(models.Model):
    comment = models.TextField(null=True)
    rate = models.IntegerField(null=True)
    tag = models.ForeignKey('Tag',null=True,on_delete=models.SET_NULL,default=None)

    def get_variables(self):
        return {
            'comment':self.comment,
            'rate':self.rate,
        }
