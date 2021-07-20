from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('test1', views.test1, name='test1'),
]
