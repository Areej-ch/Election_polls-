from django.urls import path
from .views import homepage, create_poll, poll_detail, poll_results, register, user_login, user_logout

urlpatterns = [
    path('', homepage, name='homepage'),
    path('create_poll/', create_poll, name='create_poll'),
    path('poll/<int:poll_id>/', poll_detail, name='poll_detail'),
    path('poll/<int:poll_id>/results/', poll_results, name='poll_results'),
    path('register/', register, name='register'),  # Registration URL
    path('login/', user_login, name='login'),      # Login URL
    path('logout/', user_logout, name='logout'),   # Logout URL
]
