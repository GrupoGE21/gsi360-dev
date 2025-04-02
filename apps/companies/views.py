from rest_framework import generics

from apps.companies.models import OperationalCompany, CompanyGroup
from apps.companies.serializers import CompanySerializer, CompanyGroupSerializer, UserSerializer
from apps.users.models import CustomUser


class CompanyGroupListCreateView(generics.ListCreateAPIView):
    queryset = CompanyGroup.objects.all()
    serializer_class = CompanyGroupSerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = OperationalCompany.objects.all()
    serializer_class = CompanySerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
