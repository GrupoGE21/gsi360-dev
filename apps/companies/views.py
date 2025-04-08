from rest_framework.viewsets import ModelViewSet
from apps.companies.models import Company, CompanyGroup, Department
from apps.companies.serializers import CompanySerializer, CompanyGroupSerializer, DepartmentSerializer


class CompanyGroupViewSet(ModelViewSet):
    queryset = CompanyGroup.objects.all()
    serializer_class = CompanyGroupSerializer
    lookup_field = 'code'


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'code'


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'code'
