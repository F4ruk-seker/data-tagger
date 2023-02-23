from django.shortcuts import render
from django.shortcuts import Http404
from django.shortcuts import redirect

from django.views.generic import View

from Auth.forms import user_login_form

from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages

import datetime
from django.utils import timezone
from Auth.models import AuthToken


from Auth.forms import TokenForum

class Logout(View):
    def post(self,request):
        response = redirect('Auth:login')
        logout(request)
        return response


class LoginView(View):
    @staticmethod
    def get_auth_token(token):
        pass
    def get(self,request):
        if request.user.is_authenticated:
            # return redirect('Data:data_list')
            return redirect('Data:data_list')
        else:
            token = request.GET.get('AuthToken')
            if token:
                try:
                    _token = AuthToken.objects.get(token=token)
                    if _token:
                        meta = request.META
                        _token.usage = f"{meta.get('REMOTE_ADDR')},"
                        _token.save()
                        login(request,_token.user)
                        return redirect('Data:data_list')
                except:
                    return render(request, template_name='login.html')
            else:
                return render(request, template_name='login.html')

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


class createLoginToken(View):

    def get(self,request):
        if request.user.is_authenticated and request.user.is_superuser:
            form = TokenForum()
            return render(request,template_name='select_user.html',context={'form':form})
        else:
            raise Http404
    def post(self,request):
        form = TokenForum(request.POST or None)
        if request.user.is_authenticated and request.user.is_superuser and form.is_valid():
            form.save(commit=False)
            token_gen = AuthToken.objects.create(
                user=form.cleaned_data.get('user'),
                life=timezone.now() + datetime.timedelta(days=5)
            )
            return render(request,template_name='select_user.html',context={'form':form,'token':token_gen})
        else:
            return Http404
