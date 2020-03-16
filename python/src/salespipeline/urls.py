from django.urls import path
from . import views

app_name = 'salespipeline'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('regist', views.regist, name='regist'),
    path('edit/<int:salespipeline_id>', views.edit, name='edit'),
]