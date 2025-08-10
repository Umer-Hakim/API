import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    employee_designation = django_filters.CharFilter(field_name='employee_designation', lookup_expr='iexact')
    employee_name = django_filters.CharFilter(field_name='employee_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='TO EMP ID')



    class Meta:
        model = Employee
        fields = ['employee_designation', 'employee_name']

    
    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(employee_id__gte = value)
        elif name == 'id_max':
            return queryset.filter(employee_id__lte = value)
        return queryset