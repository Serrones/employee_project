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
