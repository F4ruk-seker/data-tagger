from django import forms
from DataManager.models import Comment


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['modified_by','rate']