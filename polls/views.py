from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404  # Ensure you import 'get_object_or_404'
from .forms import PollForm
from .models import Poll, Choice

def homepage(request):
    return render(request, 'polls/homepage.html')  # Updated path


def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save()
            options = form.cleaned_data['options'].split(',')
            for option in options:
                Choice.objects.create(poll=poll, choice_text=option.strip())
            return redirect('poll_detail', poll_id=poll.id)
    else:
        form = PollForm()
    return render(request, 'polls/create_poll.html', {'form': form})  # Updated path

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choices = poll.choice_set.all()  # Use reverse relation to get choices
    return render(request, 'polls/poll_detail.html', {'poll': poll, 'choices': choices})

def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choices = poll.choice_set.all()
    results = {
        'question': poll.question,
        'votes': [choice.votes for choice in choices],
    }
    return JsonResponse(results)
