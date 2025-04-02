from django.urls import path
from apps.companies import views

urlpatterns = [
    path('groups/', views.CompanyGroupListCreateView.as_view(), name='group-list-create'),
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list-create'),
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
]
