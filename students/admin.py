from django.contrib import admin
from . models import Student


# admin.site.register(Student)





class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'student_branch')
    search_fields = ('student_name',)



admin.site.register(Student, StudentAdmin)




