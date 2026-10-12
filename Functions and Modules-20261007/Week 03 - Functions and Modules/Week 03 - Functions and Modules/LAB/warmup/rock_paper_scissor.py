"""
Rock, Paper, Scissors
Uses: functions, return, random.randint()

At the top of your file, write import random.
Define a function called get_computer_choice().
Inside it, create a variable number and set it to random.randint(0, 2).
Use if/elif/else to check number:
if it is 0, return "rock"
if it is 1, return "paper"
otherwise, return "scissors"
Define a function called decide_winner(user_choice, computer_choice).
Inside it, if user_choice equals computer_choice, return "draw".
Add an elif that returns "user" if the user wins (rock beats scissors, paper beats rock, scissors beats paper).
Add an else that returns "computer".
Outside the functions, use input() to ask the user for their choice and store it in a variable called user_choice.
Call get_computer_choice() and store the result in computer_choice.
Print the computer's choice.
Call decide_winner(user_choice, computer_choice) and store the result in winner.
Print who won.
"""

import random


def get_computer_choice():
    number = random.randint(0, 2)
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    else:
        return "scissors"


def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"


user_choice = input("Enter rock, paper, or scissors: ")
computer_choice = get_computer_choice()
print("Computer chose:", computer_choice)

winner = decide_winner(user_choice, computer_choice)
if winner == "draw":
    print("It's a draw!")
else:
    print("The winner is:", winner)


    