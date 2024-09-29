from django.db import models

POLL_TYPE_CHOICES = [
    ('multiple_choice', 'Multiple Choice'),
    ('word_cloud', 'Word Cloud'),
    ('quiz', 'Quiz'),
    ('rating', 'Rating Poll'),
    ('open_text', 'Open Text'),
    ('ranking', 'Ranking Poll'),
    ('survey', 'Survey'),
]

class Poll(models.Model):
    title = models.CharField(max_length=200)
    poll_type = models.CharField(max_length=50, choices=POLL_TYPE_CHOICES)
    question = models.TextField()
    options = models.TextField(help_text='Enter options separated by commas.', default='No options available.')  # Default value added

    def __str__(self):
        return self.title

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

