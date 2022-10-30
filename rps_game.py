import random


def winner(player_counter, computer_counter):
    if player_counter < computer_counter:
        return "Computer"
    else:
        return "Player"


choices = ["rock", "paper", "scissors"]
rounds = 0
while rounds <= 0:
    rounds = int(input("How many rounds needed to win?: "))


print("The first one to win " + str(rounds) + " rounds wins the game")

while True:

    counter = 0
    player_wins = 0
    computer_wins = 0

    while player_wins < rounds and computer_wins < rounds:

        player = None
        computer = random.choice(choices)

        while player not in choices:
            player = input("Rock, Paper or Scissors?:").lower()

        if player == computer:
            print("Computer plays: " + computer)
            print("Your play: " + player)
            print("It's a draw!")
            counter += 1
        elif player == "rock":
            if computer == "paper":
                print("Computer plays: " + computer)
                print("Your play: " + player)
                print("You lose! :(")
                computer_wins += 1
                counter += 1
            if computer == "scissors":
                print("Computer plays: " + computer)
                print("Your play: " + player)
                print("You win! :)")
                player_wins += 1
                counter += 1
        elif player == "paper":
            if computer == "rock":
                print("Computer plays: " + computer)
                print("Your play: " + player)
                print("You win! :)")
                player_wins += 1
                counter += 1
            if computer == "scissors":
                print("Computer plays: " + computer)
                print("Your play: " + player)
                print("You lose! :(")
                computer_wins += 1
                counter += 1
        elif player == "scissors":
            if computer == "paper":
                print("Computer plays: " + computer)
                print("Your play: " + player)
                print("You win! :)")
                player_wins += 1
                counter += 1
            if computer == "rock":
                print("Computer plays: " + computer)
                print("Your play: " + player)
                print("You lose! :(")
                computer_wins += 1
                counter += 1

    game_winner = winner(player_wins, computer_wins)
    print("The game has ended. The winner is... " + game_winner)

    restart = input("Do you want to play again?: (yes/no)").lower()
    if restart != "yes":
        break
    print("Bye!!")
