#!/usr/bin/env python3
# choose random number then guess it and give hints to it and keep the number of guesses and display at the end of the game
import random as rd
# main function
def main():
    # variable setting
    computer_choice, wrong_guess_count = rd.randint(1,9), 0
    # print the way to exit the game 
    print("At any point you can always type e to exit the game :3\n")
    while True:
        # the loop goes on forever giving u forever many guesses to guess the number
        # get the user guess : 
        user_guess = ""
        while not user_guess.isdigit():
            user_guess = input("Guess a random number between 1 and 9 : ")
        # convert to integer
        user_guess = int(user_guess)
        # add to wrong guess count if its wrong
        if computer_choice != user_guess:
            wrong_guess_count += 1
        # exit loop if correct : 
        if computer_choice == user_guess:
            print("You guessed right daddy UwU congratz for you !")
            # print the number of guesses
            print(f"it took you : {wrong_guess_count} guesses to guess correctly :3")
            break
        elif computer_choice < user_guess:
            print("You over it damn guess again")
        elif computer_choice > user_guess:
            print("You below it damn guess again")
    # this is after the break statement in da loop UwU
    # ask da user if he wants to try another guessing round :
    if input("\nwould you like to play another guessing round : ") == "yes":
        # recursive function
        main()

main()
