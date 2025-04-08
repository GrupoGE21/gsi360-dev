from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.companies.views import CompanyViewSet, CompanyGroupViewSet, DepartmentViewSet

router = DefaultRouter()
router.register("company", CompanyViewSet)
router.register("companygroup", CompanyGroupViewSet)
router.register("department", DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
