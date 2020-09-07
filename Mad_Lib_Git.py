#This initial for-loop is an intro to the game.
n = input("Would you like to play a Mad Lib?: ")
if n == "yes":
    print("Excellent!")
elif n == "no":
    print("Are you sure...? Give it a try! ")


#This function contains the code for my mad lib and uses the format method to store the user's input.
def Game():
    print("There once was an {} from Orono. Who {} in a tree atop a large {}".format(v1, v2, v3))
v1 = input("Please enter a adjective: ")
v2 = input("Let's try a verb this time: ")
v3 = input("Okay... one more adjective: ")
print("Thanks for playing!")

#Calling the function to run the code and play the game.
Game()
