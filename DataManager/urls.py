from django.urls import path
from DataManager.views import AllData,get_data_detail_from_name,set_data_tag

app_name = "Data"
urlpatterns = [

    path('',AllData.as_view(),name='data_list'),
    path('<slug:slug>',get_data_detail_from_name,name='data_detail'),
    path('<str:name>/set_tag/<str:_id>',set_data_tag,name='data_tag'),
]
