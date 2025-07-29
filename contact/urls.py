from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),

    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    path('user/create/', views.register, name='register'),
    path('user/login/', views.login, name='login'),
    path('user/logout/', views.logout, name='logout'),
    #path('user/delete/', views.register, name='register'),
]
