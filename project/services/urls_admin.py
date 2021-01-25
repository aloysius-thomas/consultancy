from django.urls import path

from .views import admin_home_view
from .views import candidate_list_view
from .views import company_create_view
from .views import company_list_view
from .views import product_launch_list
from .views import vacancy_list_view

urlpatterns = [
    path('', admin_home_view, name='admin-home'),
    path('human-resource/company/add/', company_create_view, name='human-resource-company-add-view'),
    path('human-resource/candidate/list/', candidate_list_view, name='human-resource-candidate-list'),
    path('human-resource/vacancy/list/', vacancy_list_view, name='human-resource-vacancy-list'),
    path('human-resource/company/list/', company_list_view, name='human-resource-company-list'),
    path('event/product-launch/list/', product_launch_list, name='event-product-launch/-list'),


]
