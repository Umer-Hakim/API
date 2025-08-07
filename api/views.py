# from django.shortcuts import render
# from django.http import JsonResponse
# from django.urls import path
from students.models import Student 
from .serializers import StudentSerializer, EmployeeSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from api import serializers
from rest_framework import mixins, generics


@api_view(['GET', 'POST'])
def studentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializers = StudentSerializer(students, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        print(serializers.errors)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    # students = Student.objects.all()
    # student_list = list(students.values())
    # return JsonResponse(student_list, safe=False)



@api_view(['GET', 'PUT', 'DELETE'])
def studentDetialsView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = StudentSerializer(student)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

    elif request.method == "PUT":
        serializers = StudentSerializer(student, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializers = EmployeeSerializers(employees, many = True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
    

#     def post(self,request):
#         seializers = EmployeeSerializers(data=request.data)
#         if serializers.as_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetails(APIView):
#     def get_object(self, pk):
#         try: 
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializers = EmployeeSerializers(employee)
#         return Response(serializers.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializers = EmployeeSerializers(employee, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_200_OK)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)


"""
#Mixxin
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


    
#Mixxin
class EmployeeDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


    def get(self, request, pk):
        return self.retrieve(request, pk)
    

    def put(self, request, pk):
        return self.update(request, pk)
    

    def delete(self, request, pk):
        return self.destroy(request, pk)

"""



class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers



class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    lookup_field = 'pk'
