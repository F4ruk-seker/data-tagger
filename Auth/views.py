from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View

from Auth.forms import user_login_form

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages

import datetime


from config.core import SessionConroller

class Logout(View):
    def post(self,request):
        response = redirect('Auth:login')
        response.delete_cookie('pars_session')
        return response

db = None
class LoginView(View):
    def get_user_from_token(self,token):
        try:
            if token:
                _token = None
                return _token.get('user')
        except:
            pass
    @staticmethod
    def login(user):
        token = db.get_database('reviews').get_collection('sessions').insert_one({
            'user': user,
            'life': datetime.datetime.utcnow() + datetime.timedelta(days=5)
        })
        response = redirect('Auth:login')
        response.set_cookie('pars_session', token.inserted_id)
        return response
    def get(self,request):
        if request.user.is_authenticated:
            # return redirect('Data:data_list')
            return redirect('Data:data_list')
        else:
            response = render(request, template_name='login.html')
            # response.delete_cookie('pars_session')
            return response

            # _token = request.GET.get('AuthToken')
            # user = self.get_user_from_token(_token)
            # if _token and user:
            #     return self.login(user)


    def post(self,request):
        form = user_login_form(request.POST or None)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('name_or_email'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request,user)
                return redirect('Data:data_list')
            else:
                messages.error(request, "login error")
                return redirect("Auth:login")
        else:
            # return render(request,template_name='login.html')
            return redirect('Auth:login')


def createLoginToken(request):

    user = db.get_database('reviews').get_collection('users').find_one({})
    _token = db.get_database('reviews').get_collection('AuthToken').insert_one({
        'user':user,
        'life':datetime.datetime.utcnow() + datetime.timedelta(days=5)
    })

    return HttpResponse(_token.inserted_id)


# old token 638308d3d72058df9a37d529