from django import forms
from DataManager.models import Tag


class TagForm(forms.ModelForm):
    name = forms.TextInput()
    explanation = forms.Textarea()

    class Meta:

        model = Tag
        fields = '__all__'

