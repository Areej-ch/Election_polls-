from django.urls import path
from .views import homepage, create_poll, poll_detail, poll_results

urlpatterns = [
    path('', homepage, name='homepage'),
    path('create_poll/', create_poll, name='create_poll'),
    path('poll/<int:poll_id>/', poll_detail, name='poll_detail'),
    path('poll/<int:poll_id>/results/', poll_results, name='poll_results'),
]
