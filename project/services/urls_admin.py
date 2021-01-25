from django.urls import path

from .views import accept_construction
from .views import accept_event
from .views import accept_tour
from .views import admin_home_view
from .views import admin_login_view
from .views import admin_logout_view
from .views import birthday_list
from .views import business_meeting_list
from .views import candidate_list_view
from .views import college_tour_list
from .views import company_create_view
from .views import company_list_view
from .views import construction_list
from .views import create_admin_view
from .views import family_tour_list
from .views import honeymoon_list
from .views import interior_2d_list
from .views import interior_3d_list
from .views import live_show_list
from .views import product_launch_list
from .views import reject_construction
from .views import reject_event
from .views import reject_tour
from .views import solo_tour_list
from .views import vacancy_list_view
from .views import wedding_list

urlpatterns = [
    path('', admin_home_view, name='admin-home'),
    path('register-admin/', create_admin_view, name='admin-register-view'),
    path('login/', admin_login_view, name='admin-login-view'),
    path('logout/', admin_logout_view, name='admin-logout-view'),
    path('human-resource/company/add/', company_create_view, name='human-resource-company-add-view'),
    path('human-resource/candidate/list/', candidate_list_view, name='human-resource-candidate-list'),
    path('human-resource/vacancy/list/', vacancy_list_view, name='human-resource-vacancy-list'),
    path('human-resource/company/list/', company_list_view, name='human-resource-company-list'),

    path('event/product-launch/list/', product_launch_list, name='event-product-launch-list'),
    path('event/business-meeting/list/', business_meeting_list, name='event-business-meeting-list'),
    path('event/live-show/list/', live_show_list, name='event-live-show-list'),
    path('event/wedding/list/', wedding_list, name='event-wedding-list'),
    path('event/birthday/list/', birthday_list, name='event-birthday-list'),
    path('event/<int:event_id>/accept/', accept_event, name='accept-event'),
    path('event/<int:event_id>/reject/', reject_event, name='reject-event'),

    path('constructions/construction/list/', construction_list, name='constructions-construction-list'),
    path('constructions/interior-2d/list/', interior_2d_list, name='constructions-interior_2d-list'),
    path('constructions/interior-3d/list/', interior_3d_list, name='constructions-interior_3d-list'),
    path('constructions/<int:construction_id>/accept/', accept_construction, name='accept-constructions'),
    path('constructions/<int:construction_id>/reject/', reject_construction, name='reject-constructions'),

    path('tour/solo/list/', solo_tour_list, name='tour-solo-list'),
    path('tour/family/list/', family_tour_list, name='tour-family-list'),
    path('tour/college/list/', college_tour_list, name='tour-college-list'),
    path('tour/honeymoon/list/', honeymoon_list, name='tour-honeymoon-list'),
    path('tour/<int:tour_id>/accept/', accept_tour, name='accept-tour'),
    path('tour/<int:tour_id>/reject/', reject_tour, name='reject-tour'),
]
