from django import forms
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
