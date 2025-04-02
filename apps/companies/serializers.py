from rest_framework import serializers
from apps.companies.models import OperationalCompany, CompanyGroup
from apps.users.models import CustomUser


class CompanyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGroup
        fields = ['id', 'name']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalCompany
        fields = ['id', 'name', 'group']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'full_name']
