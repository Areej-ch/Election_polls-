from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import PollForm, UserRegistrationForm, UserLoginForm
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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('homepage')  # Redirect to homepage or any other page
    else:
        form = UserRegistrationForm()
    return render(request, 'polls/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  # Redirect to homepage or any other page
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'polls/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('homepage')  # Redirect to homepage after logging out
