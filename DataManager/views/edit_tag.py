from DataManager.models import Tag

from django.views.generic import View

from DataManager.forms import TagForm

from django import shortcuts

class TagEdit(View):
    @staticmethod
    def get_tag_from_id(id):
        try:
            return Tag.objects.get(id=id)
        except:
            pass
    def get(self,request):
        _tag = request.GET.get('tag')
        tag = self.get_tag_from_id(_tag)
        if _tag and tag:

            form = TagForm(instance=tag)
        else:
            form = TagForm()
        return shortcuts.render(request, 'tag_form.html', context={'tag': tag or None, 'form': form})

    def post(self,request):
        _tag = request.GET.get('tag')
        tag = self.get_tag_from_id(_tag)
        if _tag and tag:
            form = TagForm(request.POST or None)
            if form.is_valid():
                tag.name = form.cleaned_data.get('name')
                tag.explanation = form.cleaned_data.get('explanation')
                tag.save()
        else:
            form = TagForm(request.POST or None)
            if form.is_valid():
                form.save(commit=False)
                Tag.objects.create(
                    name=form.cleaned_data.get('name'),
                    explanation=form.cleaned_data.get('explanation'))
        return shortcuts.redirect('Data:edit_tag')
