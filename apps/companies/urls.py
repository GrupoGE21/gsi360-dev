from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.companies.views import Company, CompanyGroup, User

router = DefaultRouter()
router.register("company", Company)
router.register("companygroup", CompanyGroup)
router.register("user", User)
urlpatterns = [
    path('', include(router.urls)),
]
