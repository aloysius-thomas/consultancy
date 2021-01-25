from django.urls import path

from .views import book_product_launch_view
from .views import construction_page_view
from .views import event_management_page_view
from .views import human_resource_page_view
from .views import marketing_view
from .views import tour_page_view

urlpatterns = [
    path('human-resource/', human_resource_page_view, name='human-resource'),
    path('event/', event_management_page_view, name='event-management'),
    path('construction/', construction_page_view, name='construction'),
    path('tour/', tour_page_view, name='tour'),
    path('marketing/', marketing_view, name='marketing'),
    path('event/product-launch/book/', book_product_launch_view, name='product-launch-booking'),
]
