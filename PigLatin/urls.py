"""
Definition of urls for ClimbingCompanion.
"""

from django.conf.urls import include, url
from PigLatin import views

urlpatterns = [
    url(r'^$', views.pigLatin, name = 'pigLatin'),

    ]