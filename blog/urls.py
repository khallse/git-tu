from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home , name='home'),
    path('article/<slug:slug>', views.detail , name='detail'),
    path('category/<slug:slug>', views.category , name='category'),
    path('page/<int:page>', views.home , name='home'),
    path('category/<slug:slug>/<int:page>', views.category, name='category'),
]
