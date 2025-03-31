from django.urls import path
from . import views

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.home, name='home'),
]
