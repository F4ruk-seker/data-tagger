from DataManager.models import Comment

from django.views.generic import View
from django import shortcuts
from django.http import JsonResponse


def CommentDelete(request,slug):
    if request.user.is_authenticated and request.method == 'POST':
        try:
            comment_id = request.POST.get('comment')
            comment = Comment.objects.get(id=comment_id)
            comment.delete = True
            Comment.modified_by = request.user
            comment.save()
            return JsonResponse(
                {"success": True, "message": f"Row : {comment.id} | DELETED"})
        except Exception as er:
            print(er)
            raise shortcuts.Http404
    else:
        raise shortcuts.Http404
