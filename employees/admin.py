from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_designation',)
    search_fields = ('employee_name',)



admin.site.register(Employee, EmployeeAdmin)
