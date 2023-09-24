from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='coalstack-home'),
    path('login/', views.login, name='coalstack-login'),
    path('history/', views.history, name='chat-history'),
    path('landing/', views.landing, name='landing'),
]
