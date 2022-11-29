from django.urls import path
from DataManager.views import AllData,get_data_detail_from_name,set_data_tag,CommentEdit
app_name = "Data"
urlpatterns = [

    path('',AllData.as_view(),name='data_list'),
    path('<slug:slug>',get_data_detail_from_name,name='data_detail'),
    path('<slug:slug>/set_tag/<str:comment_id>',set_data_tag,name='data_tag'),
    path('<slug:slug>/edit_comment/<str:comment_id>',CommentEdit,name='comment_edit'),
]
