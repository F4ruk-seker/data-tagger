from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import Http404
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic import UpdateView

from pymongo.collection import ObjectId
from django.db.models import Q
from DataManager.models import Reviews
from DataManager.models import Tag
from DataManager.models import Comment

from DataManager.forms import CommentUpdateForm
import json
from config.core.SessionConroller import get_auth_user
db = None
class AllData(View):
    def get(self,request):
        if request.user.is_authenticated:
            data_list = Reviews.objects.all()
            return render(request,template_name='view_all_data.html',context={'data_list':data_list})
        else:
            return redirect('Auth:login')

def get_data_detail_from_name(request,slug):

    if request.user.is_authenticated:
        try:
            data_list = Reviews.objects.get(slug=slug)
            print(data_list)
            return render(request,template_name='data.html',context={'database_detail':None,'data_list':data_list,'tag_list':Tag.objects.all()})
        except Exception as e:
            print(f'except from data view {e}' )
            raise Http404()
    else:
        return redirect('Auth:login')

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
                    raise Http404(json.dumps({"success":False,"message":f"Tag 404 {request.POST.get('tag')}"}))

            except Exception as er:
                print(er)
                raise Http404('document not found')
    else:
        return redirect('Auth:login')
    raise Http404

def CommentEdit(request,slug,comment_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                comment = Comment.objects.get(id=comment_id)
                form = CommentUpdateForm(request.POST or None,instance=comment)
                if form.is_valid():
                    form.save()
                    return render(request,'edit_comment.html',context={'form':form})
                else:Http404('save fail')
            except Exception as er:
                print(er)
                raise Http404('document not found')
        else:
            try:
                comment = Comment.objects.get(id=comment_id)
                form = CommentUpdateForm(instance=comment)
                return render(request,'edit_comment.html',context={'form':form})
            except:
                raise Http404('document not found')
    else:
        return redirect('Auth:login')
