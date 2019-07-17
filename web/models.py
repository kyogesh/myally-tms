from django.db import models
from django.contrib.auth import get_user_model


year_choices = [('First', 'First'), ('Second', 'Second'),
                ('Third', 'Third'), ('Fourth', 'Fourth')]

User = get_user_model()


class Department(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.CharField(max_length=50, choices=year_choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    residential_status = models.CharField(max_length=100)
    email = models.EmailField()

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name


class Template(models.Model):

    title = models.CharField(max_length=200)
    year = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    residential_status = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
