from django.test import TestCase
from employee_manager.models import ProfileEmployee


class TestProfileEmployee(TestCase):
    """ Test module for Profile_Employee model """

    def setUp(self):
        ProfileEmployee.objects.create(
            name='Casper', email='casper@email.com', department='Testes')
        ProfileEmployee.objects.create(
            name='Muffin', email='muffin@email.com', department='Testes')

    def test_employee(self):
        employee_casper = ProfileEmployee.objects.get(name='Casper')
        employee_muffin = ProfileEmployee.objects.get(name='Muffin')
        self.assertEqual(
            employee_casper.department, "Testes")
        self.assertEqual(
            employee_muffin.department, "Testes")
