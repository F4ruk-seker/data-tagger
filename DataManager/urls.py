from django.urls import path
from DataManager.views import AllData,get_data_detail_from_name,set_data_tag,CommentEdit,CommentDelete,download_data
app_name = "Data"

urlpatterns = [
    path('',AllData.as_view(),name='data_list'),
    path('<slug:slug>/',get_data_detail_from_name,name='data_detail'),
    path('<slug:slug>/set_tag/<str:comment_id>',set_data_tag,name='data_tag'),
    path('edit_comment/<str:comment_id>',CommentEdit,name='comment_edit'),
    path('<slug:slug>/delete_comment',CommentDelete,name='comment_delete'),
    path('<slug:slug>/download_data/<str:data_type>',download_data,name='download_data'),
]
