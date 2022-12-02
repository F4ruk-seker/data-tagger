from DataManager.forms import CommentUpdateForm

from DataManager.models import Comment

from django import shortcuts

def CommentEdit(request,comment_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                comment = Comment.objects.get(id=comment_id)
                form = CommentUpdateForm(request.POST or None,instance=comment)
                if form.is_valid():
                    form.save()
                    return shortcuts.render(request,'edit_comment.html',context={'form':form})
                else:
                    raise shortcuts.Http404('save fail')
            except:
                raise shortcuts.Http404('document not found')
        else:
            try:
                comment = Comment.objects.get(id=comment_id)
                form = CommentUpdateForm(instance=comment)
                return shortcuts.render(request,'edit_comment.html',context={'form':form})
            except:
                raise shortcuts.Http404('document not found')
    else:
        return shortcuts.redirect('Auth:login')
