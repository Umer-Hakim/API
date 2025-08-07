from django.http import HttpResponse
from django.shortcuts import render



def students(request):
    student=[
        {'id':1, 'name': 'Umer', 'age': 25}
    ]
    return HttpResponse(student)