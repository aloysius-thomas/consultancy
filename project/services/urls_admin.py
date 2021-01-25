from django.urls import path

from .views import admin_home_view
from .views import company_create_view

urlpatterns = [
    path('', admin_home_view, name='admin-home'),
    path('company/add/', company_create_view, name='company-add-view'),
]
