from django.views.generic import View
from DataManager.models import Tag

from django.http import JsonResponse
from django import shortcuts

class Remove_tag(View):
    @staticmethod
    def get_tag_from_id(id):
        try:
            return Tag.objects.get(id=id)
        except:
            pass
    def post(self,request):
        try:
            _tag = request.POST.get('tag_id')
            tag = self.get_tag_from_id(_tag)
            tag_name = tag.name
            tag.delete()
            return JsonResponse(
                {"success": True, "message": f"Tag : {tag_name} | DELETED"})
        except:
            raise shortcuts.Http404