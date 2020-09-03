from random import randint


options = ["Rock", "Paper", "Scissors"]

computer = options[randint(0, 2)]

print("Options: 1 = Rock , 2 = Paper, 3 = Scissors")
player = input("Choose your option number:")

if player == "1":
    print("You chose Rock, and the computer chose " + computer)
elif player == "2":
    print("You chose Paper, and the computer chose " + computer)
elif player == "3":
    print("You chose Scissors, and the computer chose " + computer)

if player == "1" and computer == "Rock":
    print("It is a draw!")
elif player == "1" and computer == "Paper":
    print("The computer wins!")
elif player == "1" and computer == "Scissors":
    print("You win!")

if player == "2" and computer == "Rock":
    print("You win!")
elif player == "2" and computer == "Paper":
    print("It is a draw!")
elif player == "2" and computer == "Scissors":
    print("The computer wins")

if player == "3" and computer == "Rock":
    print("The computer wins!")
elif player == "3" and computer == "Paper":
    print("You win!!")
elif player == "3" and computer == "Scissors":
    print("It is a Draw")
