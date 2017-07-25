from django.conf.urls import url
from upload_demographic import views

urlpatterns = [
    url(r'^upload_demog', views.demog_upload_view, name='uploadDemog'),
]