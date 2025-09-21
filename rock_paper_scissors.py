import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

rock = "✊ - rock"
paper = "✋ - paper"
scissors = "✌️ - scissors"

human_score = 0
machine_score = 0
print("Welcome to the Ultimate Rock, Paper, Scissors Showdown! ✊✋✌️\n"
      "Step into the arena where quick wits and sharp instincts rule. \n"
      "Will you crush with Rock, outsmart with Paper, or strike fast with Scissors?\n"
      "Every choice counts — so think fast, play bold, and claim your victory!\n")
print("👉 Ready? The game is simple. The thrill? Endless.")

while True:
    player_move = input("\nChoose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")
    print(f"\nYou chose: {player_move}.")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose: {computer_move}.\n")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!")
        human_score += 1
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        print(Fore.RED + "You lose!")
        machine_score += 1
    print(f"\nCurrent score:\nHuman: {human_score}\nMachine: {machine_score}\n")
    continue_game = input("Do you want to continue playing? Type Yes or No: ")
    print()
    if continue_game == "Yes" or continue_game == "yes" or continue_game == "y":
        continue
    else:
        print(f"\nThanks for playing! Final score:\nHuman: {human_score}\nMachine: {machine_score}\n")
        if human_score > machine_score:
            print("Victory for mankind!")
        elif human_score == machine_score:
            print("Better luck next time - it was a DRAW!")
        else:
            print("Victory for the machines!")
    break
