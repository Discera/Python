import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None
    restart = None
    while player not in choices:
        player = input("rock, paper or scissors? :").lower()

    print("Player: " + player)
    print("Computer: " + computer)

    if player == computer:
        print("Tie!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    elif player == "scissors" and computer == "rock":
        print("Computer wins!")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "rock" and computer == "paper":
        print("Computer wins!")
    elif player == "paper" and computer == "scissors":
        print("Computer wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")

    while restart != "yes" and restart != "no":
        restart = input("Do you want to play again? yes or no :").lower()
    if restart != "yes":
        break
print("Bye!")
