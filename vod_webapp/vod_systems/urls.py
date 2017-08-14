from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views

from vod_systems import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^updemo/', include('upload_demo.urls')),
    url(r'^vod/', include('vod_webapp.urls')),
    url(r'^not$', views.not_implemented, name='not-imp'),

    url(r'^$', views.landing, name='index'),
]