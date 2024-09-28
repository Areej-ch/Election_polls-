from django.contrib import admin
from .models import Poll, Choice  # Ensure you are importing the correct models

admin.site.register(Poll)
admin.site.register(Choice)
