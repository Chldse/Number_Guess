print(""" Let's see if you can read my mind!
I am thinking of a number between 1 and 20""")

def num_guess():
    secret_num = "19"
    user_guess = ""
#Setting guess count to zero so that counts can be added on as user guesses.
    guess_count = 0
#The guess_limit variable stores the number of times I am allowing the user to take a guess.
    guess_limit = 3
#Setting no_guesses variable to false to begin becasue when it becomes true, game ends.
    no_guesses = False
###This while loop is saying: if the user has not guessed the correct answer and
###the user still has guesses avaiable it will iterate through the if statement until
###the conditions of the if-statement are met or the answer is guessed correctly.
    while user_guess != secret_num and not (no_guesses):
        if guess_count < guess_limit:
            user_guess = input("Take a guess! ")
            guess_count += 1
###If the conditons of the if-statement have not been met, the no_guesses variable
### are set to True, saying the user is out of guesses and the 2nd if-statement
### will print an ending message.
        else:
            no_guesses = True
    if no_guesses:
        print("You've lost user, I am sorry")
    else:
        print("Congratulations! You're a mind reader. ")
####If the user guesses correctly and the no_guesses variable is still false
### the else will print out a celebratory message.

num_guess()
