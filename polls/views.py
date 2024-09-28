from django.shortcuts import render, redirect
from .models import Poll
from .forms import PollForm

def homepage(request):
    return render(request, 'polls/homepage.html')  # Render homepage

def create_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to homepage after saving
    else:
        form = PollForm()
    return render(request, 'polls/create_poll.html', {'form': form})  # Render the create poll form
