from rest_framework import serializers
from apps.companies.models import Company, CompanyGroup, Department
from apps.users.models import User


class CompanyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGroup
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'