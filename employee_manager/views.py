from .models import ProfileEmployee
from django.views.generic import ListView, DetailView

class EmployeeList(ListView):
    """
    Employees List Class
    """
    queryset = ProfileEmployee.objects.order_by('name')
    template_name = 'employee_manager/index.html'


class EmployeeDetail(DetailView):
    """
    Employee Detail Class, with a little test, in case of a employee that
    doesn't exist
    """
    model = ProfileEmployee
    template_name = 'employee_manager/detail.html'
