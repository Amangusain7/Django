from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('',views.TodoView.as_view(),name='todo'),
]