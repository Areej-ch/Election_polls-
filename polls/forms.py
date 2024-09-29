from django import forms
from django.contrib.auth.models import User
from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'poll_type', 'question', 'options']
        widgets = {
            'poll_type': forms.Select(choices=[
                ('multiple_choice', 'Multiple Choice'),
                ('word_cloud', 'Word Cloud'),
                ('quiz', 'Quiz'),
                ('rating', 'Rating Poll'),
                ('open_text', 'Open Text'),
                ('ranking', 'Ranking Poll'),
                ('survey', 'Survey'),
            ]),
            'options': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter comma-separated options'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
