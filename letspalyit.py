"""
hey everyone, this is a simple rock paper scissors game.
you can play it with your friends or against the computer.

win the game by choosing rock, paper, or scissors.

rock beats scissors
scissors beats paper
paper beats rock

if you choose the same as the computer, it's a tie.

caution : human build the computer not the computer build the human. 
win the game human  are mind and computer is machine.
computer just based on predictions

let's play!


"""

import random

print("Welcome to Rock, Paper, Scissors!")
print("let's play it with computer")

maker_list = ["rock", "paper", "scissors"]

while True:
    user_choice = input("enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(maker_list)

    print(f"user choice: {user_choice} | computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("both are same = that match is tie")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("rock beats scissors = you win")
        else:
            print("paper beats rock = you lose")

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("paper beats rock = congratulations you win ")
        else:
            print("scissors beats paper  = sorry you lose ")

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("scissors beats paper = you win")
        else:
            print("rock beats scissors = you lose")

    else:
        print("invalid choice, please choose rock, paper, or scissors")

        play_again = input("do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    

  
print("Thanks for playing! Goodbye!")
print("if you want to play again then run the code again")
print("if you want to play with your friend then share this code with him/her")
print("if you want to play with your friend then share this code with him/her")
print("if you want to play with your friend then share this code with him/her")