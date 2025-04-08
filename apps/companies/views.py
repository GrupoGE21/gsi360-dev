from rest_framework.viewsets import ModelViewSet
from apps.companies.models import Company, CompanyGroup
from apps.companies.serializers import CompanySerializer, CompanyGroupSerializer


class CompanyGroup(ModelViewSet):
    queryset = CompanyGroup.objects.all()
    serializer_class = CompanyGroupSerializer
    lookup_field = 'code'


class Company(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'code'
