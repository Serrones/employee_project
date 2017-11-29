"""
Good use of Curl in this project:

get all -- curl -u "username" -H "Content-Type: application/javascript" "http://127.0.0.1:8000/api/employee/"

get a specific employee --
    curl -u "username" -H "Content-Type: application/javascript" "http://127.0.0.1:8000/api/employee/id_number/"

post -- curl -u "username" -d "{"name":"NAME", "email":"email@email.com","department":"DEPARTAMENTO"}"
            -H "Content-Type:application/javascript" -X POST "http://127.0.0.1:8000/api/employee/"

put -- curl -u "username" -d '{"name":"NAME", "email":"email@email.com",
            "department":"Department"}' -H "Content-Type:application/javascript"
            -X PUT "http://127.0.0.1:8000/api/employee/id_number/"

delete -- curl -u "username" -X DELETE "http://127.0.0.1:8000/api/employee/id_number/"

"""

from employee_manager.models import ProfileEmployee
from rest_framework import serializers


class ProfileEmployeeSerializer(serializers.ModelSerializer):
    """
    This class is used for defining the model that we want serializer and
    pass foward for external applications used
    """
    class Meta:
        # Model choosen
        model = ProfileEmployee
        # Fields choosen
        fields = '__all__'
