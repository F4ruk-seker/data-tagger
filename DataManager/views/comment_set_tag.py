from DataManager.models import Tag
from DataManager.models import Comment

from django import shortcuts
from django.http import JsonResponse

import json


def set_data_tag(request,slug:str,comment_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                tag_id = request.POST.get('tag')
                tag = Tag.objects.get(id=tag_id)
                if tag_id and tag:
                    comment = Comment.objects.get(id=comment_id)
                    comment.tag = tag
                    comment.modified_by = request.user
                    comment.save()

                    return JsonResponse({"success":True,"message":f"Row : {comment.id} |-> {tag.name}","update_by":request.user.username})
                else:

                    raise shortcuts.Http404(json.dumps({"success":False,"message":f"Tag 404 {request.POST.get('tag')}"}))
            except Exception as e:
                print(e)
                raise shortcuts.Http404('document not found')
    else:
        return shortcuts.redirect('Auth:login')
    raise shortcuts.Http404
