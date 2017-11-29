from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from employee_api import views as profile_views

# API's router
router = DefaultRouter()
router.register(r'employee',profile_views.ProfileEmployeeViewSet)

# Basic router, for admin, list and details html pages
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employee_manager/', include('employee_manager.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^', include('employee_api.urls')),
]
