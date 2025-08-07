from django.db import models

class Student(models.Model):
    student_id     = models.CharField(max_length=20)
    student_name   = models.CharField(max_length=20)
    student_branch = models.CharField(max_length=20)


    def __str__(self):
        return self.student_name
