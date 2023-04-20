from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# pass


class Comment(models.Model):
    comment = models.TextField(null=True)
    rate = models.IntegerField(null=True,validators=[MinValueValidator(0),
                                       MaxValueValidator(5)],default=0)
    tag = models.ForeignKey('Tag',null=True,on_delete=models.SET_NULL,default=None)

    modified_by = models.ForeignKey('Account.CustomUserModel',on_delete=models.SET_NULL,default=None,null=True,blank=True)

    last_update = models.DateTimeField(auto_now=True)
    delete = models.BooleanField(default=False)

    def get_variables(self):
        return {
            'comment':self.comment,
            'rate':self.rate,
            'modified_by':self.modified_by
        }

    def __str__(self):
        if self.comment:
            return f'{self.comment[:150]}...'
        return "Err paresed"

