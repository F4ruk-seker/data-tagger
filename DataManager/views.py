from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import Http404
from django.http import JsonResponse
from django.views.generic import View

from pymongo.collection import ObjectId

from DataManager.models import Reviews
from DataManager.models import Tag


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
            return render(request,template_name='data.html',context={'database_detail':None,'data_list':data_list,'tag_list':Tag.objects.all()})
        except Exception as e:
            print(f'except from data view {e}' )
            raise Http404()
    else:
        return redirect('Auth:login')

def set_data_tag(request,_id:str,id:int):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                return JsonResponse({"success":True,"message":f"{_id} |-> {None.get('name')}"})
            # else:
            #     raise Http404(json.dumps({"success":False,"message":f"Tag 404 {request.POST.get('tag')}"}))

            except:
                raise Http404('document not found')
    else:
        return redirect('Auth:login')
    raise Http404
