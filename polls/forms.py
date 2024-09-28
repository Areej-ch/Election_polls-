from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two']  # Ensure all fields are listed here
