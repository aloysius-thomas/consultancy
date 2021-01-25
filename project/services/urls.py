from django.urls import path

from .views import construction_page_view
from .views import event_management_page_view
from .views import human_resource_page_view

urlpatterns = [
    path('human-resource/', human_resource_page_view, name='human-resource'),
    path('event-management/', event_management_page_view, name='event-management'),
    path('construction/', construction_page_view, name='construction'),
]
