
print("You're jolted awake by the sudden breaking of a train car.")
print("The interior lights contrasted against the pitch black windows make you wonder... \'am I in a tunnel, or is it night?\'")

def train():
    player_path = input("Do you, try to get a better look out the windows or check your phone? Please choose: ")

    if "windows" or "window" in player_path:
        print("Cupping your your hands around your face, pressing against the cold, scratched plexiglass yields no view.")
        print("Though you get the uneasy feeling something, or someone has a clear view of you.\n Illuminated by the interior lights of the train car.")
        window()
#This elif statement will not trigger, not exactly sure why..
    elif "check phone" or "phone" in player_path:
        phone_path_1()

    else:
        print("Fine, but you're no fun.")


def window():
    print("Despite your fears of an entity lurking out in the darkeness you attemp you pry open the train car doors")
    print("Having no luck using brute force, you make your way to the conductors train car.")
    print("Upon reaching the cab, you notice a keypad which unlocks the conductors cab.")

    door_code = "2920"
    user_guess = ""
    guess_count = 0
    guess_limit = 3
    no_guesses = False
#While loop is not working.... won't detect that user_guess == door_code...
#Fixed... didn't make value stored in door_code variable a string! xD
    while user_guess != door_code and not(no_guesses):
        if guess_count < guess_limit:
            guess_count += 1
            user_guess = input("Try a 4-digit code and see if the door will unlock: ")

        else:
            no_guesses = True

    if no_guesses:
        print("Please find another way")
        phone_path_2()

    else:
        print("Door Unlocked")

def phone_path_1():
    user_call = input("Who would you like to call? 1, 2, or 3? ")
    if user_call == 1:
        print("Calling: Karen")
    elif user_call == 2:
        print("Calling: Jim")
    elif user_call == 3:
        print("Pam")
    else:
        print("No Signal...")


def phone_path_2():
    print("With no luck unlocking the door, you look down at your phone.")
    print("Suddenly, a distant, rhythmic ringing begins. As it goes on it gets louder and louder.")
    print("In an instant you see shadows of a desk, televison and realize... you've awoken from a dear.")
    print("Phew! Thanks for playing!")







train()
