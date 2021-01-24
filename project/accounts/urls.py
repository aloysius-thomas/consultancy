from django.urls import path

from .views import LoginCustomView
from .views import logout_view
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginCustomView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
