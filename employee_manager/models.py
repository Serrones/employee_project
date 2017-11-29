from django.db import models

class ProfileEmployee(models.Model):
    """ This is the main class of the project. The goal is create a database
    which can storage the employee's details
    """

    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    department = models.CharField(max_length=30, unique=False, verbose_name='Departamento')

    # Function used to display the employee's name in the admin page
    def __str__(self):
        return self.name
