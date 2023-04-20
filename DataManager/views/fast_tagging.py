from DataManager.models import Tag
from DataManager.models import Reviews
from DataManager.models import Comment

from django.views.generic import View

from DataManager.forms import TagForm
from DataManager.forms import CommentUpdateForm

from django import shortcuts
from django.shortcuts import get_object_or_404
from django.views.generic import View


class FastTag(View):
    @staticmethod
    def get_colored_tags():
        tag_colors = ['btn-success', 'btn-danger', 'btn-warning', 'btn-info', 'btn-primary', 'btn-secondary']
        colored_tags = []
        counter = 0
        for tag in Tag.objects.all().order_by('id'):
            if counter > len(tag_colors) - 1:
                counter = 0
            colored_tags.append({
                'id': tag.id,
                'name': tag.name,
                'color': tag_colors[counter]
            })
            counter += 1
        return colored_tags

    @staticmethod
    def get_review_object_from_slug(slug):
        try:
            return Reviews.objects.get(slug=slug)
        except:
            pass

    def get(self,request,slug,row):
        review = self.get_review_object_from_slug(slug)
        if review:
            row_count = review.get_comment_count()
            if row >= row_count:
                raise shortcuts.Http404('Bu row dan sonra yorum yok')
            else:
                comment = review.get_comments()[row]
                return shortcuts.render(request, 'fast_tag.html',
                                        context={'tags':self.get_colored_tags(),
                                                 'comment':comment,'row':row,
                                                 'row_count':row_count,"review_stats":review.get_stats()})

        else:
            raise shortcuts.Http404('Data Sınıfı Bulunamadı')

    def post(self,request,slug,row):

        review = self.get_review_object_from_slug(slug)
        if review.get_comment_count() > row+1:
            row += 1

        comment_id = request.POST.get('id', None)
        comment_obj_instance = get_object_or_404(Comment, id=comment_id)
        comment_form = CommentUpdateForm(request.POST or None,instance=comment_obj_instance)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.modified_by = request.user
            form.save()

        return shortcuts.redirect('Data:fast_tag',slug,row)