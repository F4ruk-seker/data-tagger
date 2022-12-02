import os
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import Http404

from django.http import JsonResponse, StreamingHttpResponse, HttpResponseNotFound, HttpResponse
from django.views.generic import View
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.db.models import Q
from DataManager.models import Reviews
from DataManager.models import Tag
from DataManager.models import Comment
from config.settings import BASE_DIR
from DataManager.forms import CommentUpdateForm
from DataManager.forms import TagForm
import json
from config.core.SessionConroller import get_auth_user

class AllData(View):
    def get(self,request):
        if request.user.is_authenticated:
            data_list = Reviews.objects.all()
            tag_list = Tag.objects.all()
            return render(request,template_name='view_all_data.html',context={'data_list':data_list,'tag_list':tag_list})
        else:
            return redirect('Auth:login')

def get_data_detail_from_name(request,slug):

    if request.user.is_authenticated:
        try:
            rw = Reviews.objects.get(slug=slug)
            if request.GET.get('show_deleted'):
                data_list = rw.get_comments()
            else:
                data_list = rw.get_comments().filter(delete=False)
            return render(request,template_name='data.html',context={'database_detail':rw,'data_list':data_list,'tag_list':Tag.objects.all()})
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

def CommentEdit(request,comment_id):
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
            raise Http404
    else:
        raise Http404


import pandas as pd
from io import BytesIO
def download_data(request,slug,data_type):
    try:
        Rw = Reviews.objects.get(slug=slug)
        if request.user.is_authenticated and Rw:
            if data_type == 'json':
                data = []
                for comment in Rw.get_comments():
                    value = {"comment": comment.comment, }
                    if comment.tag == None:
                        value["tag"] = None
                    else:
                        value["tag"] = comment.tag.name
                    data.append(json.dumps(value))
                response = HttpResponse(str(data), content_type='application/vnd.ms-json')
                response['Content-Disposition'] = f'attachment; filename="{slug}.json"'
            elif data_type == 'xlsx':
                with BytesIO() as b:
                    # Use the StringIO object as the filehandle.
                    writer = pd.ExcelWriter(b, engine='xlsxwriter')
                    df = pd.DataFrame({
                        'comments':[comment.comment for comment in Rw.get_comments()],
                        'tag':[comment.tag for comment in Rw.get_comments()]
                    })
                    df.to_excel(writer, sheet_name=slug)
                    writer.save()
                    # Set up the Http response.
                    filename = f'{slug}.xlsx'
                    response = HttpResponse(
                        b.getvalue(),
                        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    )
                    response['Content-Disposition'] = 'attachment; filename=%s' % filename
                    return response
            else:
                raise Http404
    except IOError:
        response = HttpResponseNotFound('<h1>File not exist</h1>')
    except Exception as e:
        print(e)
        raise Http404
    return response


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
        return render(request, 'tag_form.html', context={'tag': tag or None, 'form': form})

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
        return redirect('Data:edit_tag')

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
            raise Http404