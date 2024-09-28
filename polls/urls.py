from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Correctly referencing the homepage view
    path('create/', views.create_poll, name='create_poll'),  # Correctly referencing the create_poll view
]
