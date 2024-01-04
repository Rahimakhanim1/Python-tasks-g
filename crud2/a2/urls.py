from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/',views.post, name='post'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('delete_checkbox',views.delete_checkbox, name="delete_checkbox"),
    path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('confirm/<int:id>',views.confirm, name='confirm'),
    path('detail/<int:id>',views.detail, name='detail'),
    path('search/',views.search, name='search'),
    path('image/',views.image,name='image'),
    path('postImg/',views.postImg,name = 'postImg'),
    # path('video/',views.video,name='video'),
    path('erp/',views.erp, name = ''),
    path('order/',views.order,name='order')

]