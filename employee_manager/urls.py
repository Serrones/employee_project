from django.conf.urls import url
from . import views



urlpatterns = [
        # Employees List url
        url(r'^$', views.index, name='index'),
        # Employee Detail url
        url(r'^(?P<ProfileEmployee_id>[0-9]+)/$', views.detail, name='detail'),

]
