from rest_framework.viewsets import ModelViewSet

from apps.companies.models import Company, CompanyGroup
from apps.companies.serializers import CompanySerializer, CompanyGroupSerializer, UserSerializer
from apps.users.models import CustomUser


class CompanyGroup(ModelViewSet):
    queryset = CompanyGroup.objects.all()
    serializer_class = CompanyGroupSerializer


class Company(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class User(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
