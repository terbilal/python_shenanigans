#!/usr/bin/env python3
# Rock Paper Scissors the game :
import random as rd
def main():
    """Main function"""
    active = True
    # score keepsaking
    player_score, computer_score = 0, 0
    rps = ["rock", "paper", "scissors"]
    # main game loop
    while active:
        # reset play choice on every loop
        player_choice = ""
        # make sure the player choice is valid
        while (player_choice not in rps): 
            player_choice = input("Plz choose rock, paper or scissors : ")
            # puppy collar option
            if player_choice == "puppy collar":
                print("Whoof Whoof")
                continue
        # game choice
        player_choice = "rock"
        game_choice = rps[rd.randint(0,2)]
        print(f"Game chose : {game_choice.title()}")
        if who_wins(player_choice, game_choice) == "tie":
            print("Its a tie")
        elif who_wins(player_choice, game_choice) == player_choice:
            player_score += 1
            print("Congratulations you wint !")
        else:
            computer_score += 1
            print("Sadge, you lost !")
        # print the scores : 
        print(f"Player score : {player_score} || Computer score : {computer_score}")
        if input(f"\nWould you like to exist the game : ") == "yes":
            active = False

def who_wins(first_choice, second_choice):
    # check if its a tie first
    if first_choice == second_choice:
        return "tie"
    # return who wins in the situation if its not a tie
    elif first_choice == "rock" and second_choice == "paper":
        return "paper"
    elif first_choice == "rock" and second_choice == "scissors":
        return "rock"
    elif first_choice == "paper" and second_choice == "rock":
        return "paper"
    elif first_choice == "paper" and second_choice == "scissors":
        return "scissors"
    elif first_choice == "scissors" and second_choice == "rock":
        return "rock"
    elif first_choice == "scissors" and second_choice == "paper":
        return "scissors"
    else:
        print("debugging mark") # debugging

# run main function : 
main()
