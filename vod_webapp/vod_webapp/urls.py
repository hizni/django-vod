from django.conf.urls import url
from vod_webapp import views

urlpatterns = [
    url(r'^login', views.login, name='vodLogin'),
]