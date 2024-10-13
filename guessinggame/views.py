from django.shortcuts import render
import random

# ask user for any whole number
# generate a random number from 0 - user input
# ask user for a random number as input
# compare generated number to user input number
# if number is correct, display congratulations message
# if number is wrong, display you lost message

# user should have 10 tries
# after each try user should be told if they are close or far from goal number



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

    return render(request, 'base.html', {
        'result': result
    })


