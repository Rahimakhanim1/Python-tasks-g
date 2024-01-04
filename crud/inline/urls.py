from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("post/",views.post,name='post'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('delete/',views.delete_checkbox,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update')
]