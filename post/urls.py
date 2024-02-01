from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'page/(\d+)$', views.index),
    re_path(r'read/(\d+)$', views.read),
    re_path(r'category/(\d+)$', views.category),
    re_path(r'archive/(\d+)/(\d+)$', views.archive),
]
