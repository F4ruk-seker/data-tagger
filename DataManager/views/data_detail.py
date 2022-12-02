from django import shortcuts

from DataManager.models import Reviews
from DataManager.models import Tag

def get_data_detail_from_name(request,slug):

    if request.user.is_authenticated:
        try:
            rw = Reviews.objects.get(slug=slug)
            if request.GET.get('show_deleted'):
                data_list = rw.get_comments()
            else:
                data_list = rw.get_comments().filter(delete=False)
            return shortcuts.render(request,template_name='data.html',context={'database_detail':rw,'data_list':data_list,'tag_list':Tag.objects.all()})
        except:
            raise shortcuts.Http404()
    else:
        return shortcuts.redirect('Auth:login')
