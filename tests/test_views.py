import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from employee_manager.models import ProfileEmployee
from employee_api.serializers import ProfileEmployeeSerializer


# initialize the APIClient app
client = Client()


class GetAllEmployeesTest(TestCase):
    """ Test module for GET all employees API """

    def setUp(self):
        ProfileEmployee.objects.create(
            name='Casper', email='casper@email.com', department='Testes')
        ProfileEmployee.objects.create(
            name='Muffin', email='muffin@email.com', department='Testes')
        ProfileEmployee.objects.create(
            name='Rambo', email='rambo@email.com', department='Testes')
        ProfileEmployee.objects.create(
            name='Ricky', email='ricky@email.com', department='Testes')

    def test_get_all_employees(self):
        # get API response
        response = client.get(reverse('get_post_employee'))
        # get data from db
        employees = ProfileEmployee.objects.all()
        serializer = ProfileEmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleEmployeeTest(TestCase):
    """ Test module for GET single employee API """

    def setUp(self):
        self.casper = ProfileEmployee.objects.create(
            name='Casper', email='casper@email.com', department='Testes')
        self.muffin = ProfileEmployee.objects.create(
            name='Muffin', email='muffin@email.com', department='Testes')
        self.rambo = ProfileEmployee.objects.create(
            name='Rambo', email='rambo@email.com', department='Testes')
        self.ricky = ProfileEmployee.objects.create(
            name='Ricky', email='ricky@email.com', department='Testes')

    def test_get_valid_single_employee(self):
        response = client.get(
            reverse('get_delete_update_employee', kwargs={'pk': self.rambo.pk}))
        employee = ProfileEmployee.objects.get(pk=self.rambo.pk)
        serializer = ProfileEmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_employee(self):
        response = client.get(
            reverse('get_delete_update_employee', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewEmployeeTest(TestCase):
    """ Test module for inserting a new employee """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'email': 'muffin@email.com',
            'department': 'Testes'
        }

        self.invalid_payload = {
            'name': '',
            'email': 'muffin@email.com',
            'department': 'Testes'
        }

    def test_create_valid_employee(self):
        response = client.post(
            reverse('get_post_employee'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_employee(self):
        response = client.post(
            reverse('get_post_employee'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleEmployeeTest(TestCase):
    """ Test module for updating an existing employee record """

    def setUp(self):
        #self.casper = Profile_Employee.objects.create(
        #    name='Casper', email='casper@email.com', department='Testes')
        self.muffin = ProfileEmployee.objects.create(
            name='Muffin', email='muffin@email.com', department='Testes')
        self.muffin = ProfileEmployee.objects.update(
            name='Muffy', email='muffy@email.com', department='Testes')
        self.valid_payload = {
            'name': 'Muffy',
            'email': 'muffy@email.com',
            'department': 'Testes'
        }

        self.invalid_payload = {
            'name': '',
            'email': 'muffy@email.com',
            'department': 'Testes'
        }

    def test_valid_update_employee(self):
        response = client.put(
            reverse('get_delete_update_employee', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_employee(self):
        response = client.put(
            reverse('get_delete_update_employee', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePuppyTest(TestCase):
    """ Test module for deleting an existing employee record """

    def setUp(self):
        self.casper = ProfileEmployee.objects.create(
            name='Casper', email='casper@email.com', department='Testes')
        self.muffin = ProfileEmployee.objects.create(
            name='Muffin', email='muffin@email.com', department='Testes')

    def test_valid_delete_employee(self):
        response = client.delete(
            reverse('get_delete_update_employee', kwargs={'pk': self.muffin.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_employee(self):
        response = client.delete(
            reverse('get_delete_update_employee', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
