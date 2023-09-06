# We will write a rock paper scissors game in class - Complete it in this file

# I went my own route for this project :)

import random

CHOICES = ["Rock", "Paper", "Scissors"]

OUTCOMES = {
    "Rock": {
        "Rock": "Tie",
        "Paper": "Lose",
        "Scissors": "Win"
    },
    "Paper": {
        "Rock": "Win",
        "Paper": "Tie",
        "Scissors": "Lose"
    },
    "Scissors": {
        "Rock": "Lose",
        "Paper": "Win",
        "Scissors": "Tie"
    }
}

def ask_for_input():
    data = input("Rock/Paper/Scissors: ").lower()
    for choice in CHOICES:
        if choice.lower()[:len(data)] == data:
            return choice
    return ""

def get_player_choice():
    while True:
        choice = ask_for_input()
        if choice: return choice
        print("Invalid input!")

player_choice = get_player_choice()
bot_choice = random.choice(CHOICES)

print("You chose", player_choice)
print("Bot chose", bot_choice)
print("Outcome:", OUTCOMES[player_choice][bot_choice])