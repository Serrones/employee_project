from django.conf.urls import url
from .views import EmployeeList, EmployeeDetail



urlpatterns = [
        # Employees List url
        url(r'^$', EmployeeList.as_view()),
        # Employee Detail url
        url(r'^(?P<pk>[0-9]+)/$', EmployeeDetail.as_view()),

]
