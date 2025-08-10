from django.shortcuts import render, get_object_or_404
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
from rest_framework import mixins, generics, viewsets
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from .pagination import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter







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

"""
#Geneics
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


#Generics
class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    lookup_field = 'pk'

"""

# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializers = EmployeeSerializers(queryset, many=True)
#         return Response(serializers.data)
    

#     def create(self, request):
#         serializers = EmployeeSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors)
    

#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializers = EmployeeSerializers(employee)
#         return Response(serializers.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializers = EmployeeSerializers(employee)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors)
    
#     def delete(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(serializers.data, status=status.HTTP_404_NOT_FOUND)




class EmployeeViewset(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    filterset_class = EmployeeFilter



class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title', 'blog_body']
    ordering_fields = ['id', 'blog_title']


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
