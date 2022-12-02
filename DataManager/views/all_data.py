from DataManager.models import Reviews
from DataManager.models import Tag

from django.views.generic import View
from django import shortcuts


class AllData(View):

    def get(self,request):
        if request.user.is_authenticated:
            data_list = Reviews.objects.all()
            tag_list = Tag.objects.all()
            return shortcuts.render(request,template_name='view_all_data.html',context={'data_list':data_list,'tag_list':tag_list})
        else:
            return shortcuts.redirect('Auth:login')
