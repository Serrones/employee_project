from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import ProfileEmployee


def index(request):
    """
    Employees List Function
    """
    employee_list = ProfileEmployee.objects.order_by('name')
    context = {'employee_list': employee_list}
    return render(request, 'employee_manager/index.html', context)

def detail(request, ProfileEmployee_id):
    """
    Employee Detail Function, with a little test, in case of a employee that
    doesn't exist
    """
    try:
        employee = ProfileEmployee.objects.get(pk=ProfileEmployee_id)
    except ProfileEmployee.DoesNotExist:
        raise Http404("Employee does not exist")
    return render(request, 'employee_manager/detail.html', {'employee': employee})
