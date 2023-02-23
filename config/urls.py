from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('Auth.urls', 'Auth')),
    path('admin/', admin.site.urls),
    path('data/',include('DataManager.urls','Data')),

]
