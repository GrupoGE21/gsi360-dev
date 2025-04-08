from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.companies.views import Company, CompanyGroup

router = DefaultRouter()
router.register("company", Company)
router.register("companygroup", CompanyGroup)

urlpatterns = [
    path('', include(router.urls)),
]
