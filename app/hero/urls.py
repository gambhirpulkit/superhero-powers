from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^visualize/$', views.visualize_data, name='visualize_data')
]
