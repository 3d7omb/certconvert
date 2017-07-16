from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/upload/')),
    url(r'^upload/$', views.upload, name='upload'),
]
