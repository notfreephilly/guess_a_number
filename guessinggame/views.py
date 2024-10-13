from django.shortcuts import render, redirect
import random
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def homepage(request):
    return render(request, "home.html")


def number_guessing_game(request):
        # checks if random number is in session, if not generate new number
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(1,  50)

    random_number = request.session['random_number'] # use the sessions random number
    result = None # this is so that the result mesage won't be shown until the user sumbits a guess

    if request.method == 'POST':
        user_guess = int(request.POST.get('guess'))

        if user_guess == random_number:
            result = "You guessed correct! Bet you can't do it again"

        elif user_guess > random_number:
            result = "Too high! Guess again"

        else:
            result = "Too low! Guess again"

    return render(request, 'game.html', {
        'result': result
    })



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})