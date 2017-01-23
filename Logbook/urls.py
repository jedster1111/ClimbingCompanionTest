from django.conf.urls import include, url
from . import views
from .views import listView2
urlpatterns = [
    #url(r'^$', views.listView, name = 'listView'),
    url(r'^$', listView2.as_view(), name = 'listView'),
    ]