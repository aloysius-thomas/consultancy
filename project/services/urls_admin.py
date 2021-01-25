from django.urls import path

from .views import company_create_view
from .views import human_resource_page_view

urlpatterns = [
    path('company/add/', company_create_view, name='company-add-view'),
]
