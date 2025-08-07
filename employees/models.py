from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=500)
    employee_name = models.CharField(max_length=500)
    employee_designation = models.CharField(max_length=500)


    def __str__(self):
        return self.employee_name
