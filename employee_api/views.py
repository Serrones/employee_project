from django.shortcuts import render
from .serializers import ProfileEmployeeSerializer
from employee_manager.models import ProfileEmployee

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


class ProfileEmployeeViewSet(viewsets.ModelViewSet):
    """
    This class have some functionalities:
        First we define the http basic authentication. With this, we can
    authenticate the user and his permissions;
        Second, we can define all the objects from the choosen database, and
    which serializer class we need to use
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = ProfileEmployee.objects.all()
    serializer_class = ProfileEmployeeSerializer

    def get(self, request, format=None):
        content= {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_employee(request, pk):
    try:
        employee = ProfileEmployee.objects.get(pk=pk)
    except ProfileEmployee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single employee
    if request.method == 'GET':
        serializer = ProfileEmployeeSerializer(employee)
        return Response(serializer.data)
    # delete a single employee
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single employee
    elif request.method == 'PUT':
         serializer = ProfileEmployeeSerializer(employee, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_employee(request):
    # get all employees
    if request.method == 'GET':
        employees = ProfileEmployee.objects.all()
        serializer = ProfileEmployeeSerializer(employees, many=True)
        return Response(serializer.data)
        # insert a new record for a employee
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'department': request.data.get('department')
        }
        serializer = ProfileEmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
