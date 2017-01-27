"""
Definition of urls for ClimbingCompanion.
"""

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from Logbook import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logbook/', include('Logbook.urls')),
    url(r'^$', views.listView, name = 'listView'),
    url(r'^piglatin/', include('PigLatin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)