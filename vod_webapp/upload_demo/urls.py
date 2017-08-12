from django.conf.urls import url
from upload_demo import views

urlpatterns = [
    url(r'^upload_demo', views.demo_upload_view, name='uploadDemo'),
]