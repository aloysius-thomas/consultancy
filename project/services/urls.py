from django.urls import path

from .views import book_birthday_view
from .views import book_business_meeting_view
from .views import book_live_show_view
from .views import book_product_launch_view
from .views import book_wedding_view
from .views import candidate_register_view
from .views import college_tour_view
from .views import construction_page_view
from .views import construction_service_view
from .views import event_management_page_view
from .views import family_tour_view
from .views import honeymoon_view
from .views import human_resource_page_view
from .views import marketing_view
from .views import solo_tour_view
from .views import tour_page_view
from .views import vacancy_submit_view

urlpatterns = [
    path('consultancy/human-resource/', human_resource_page_view, name='human-resource'),
    path('event/', event_management_page_view, name='event-management'),
    path('construction/', construction_page_view, name='construction'),
    path('tour/', tour_page_view, name='tour'),
    path('marketing/', marketing_view, name='marketing'),
    path('event/product-launch/book/', book_product_launch_view, name='product-launch-booking'),
    path('event/business-meeting/book/', book_business_meeting_view, name='business-meeting-booking'),
    path('event/live-show/book/', book_live_show_view, name='live-show-booking'),
    path('event/wedding/book/', book_wedding_view, name='wedding-booking'),
    path('event/birthday/book/', book_birthday_view, name='birthday-booking'),
    path('construction/<str:service>/book/', construction_service_view, name='construction-service-booking'),
    path('tour/solo-tour/book/', solo_tour_view, name='solo-tour-booking'),
    path('tour/family-tour/book/', family_tour_view, name='family-tour-booking'),
    path('tour/college-tour/book/', college_tour_view, name='college-tour-booking'),
    path('tour/honeymoon/book/', honeymoon_view, name='honeymoon-booking'),
    path('consultancy/register-candidate/', candidate_register_view, name='register-candidate'),
    path('consultancy/submit-vacancy/', vacancy_submit_view, name='submit-vacancy'),

]
