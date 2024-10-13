from django.shortcuts import render, redirect
import random
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


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
            messages.success(request, "Registration successful! You are now logged in")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("profile")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})



def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")





def profile(request):
    return render(request, "profile.html")