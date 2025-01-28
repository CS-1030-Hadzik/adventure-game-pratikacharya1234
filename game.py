"""
DOCS String
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")


# Ask for Player Name
player_name = input("What is your name? ")
print("Hello, " + player_name + "!")


# Concatenate Strings to create a personalized message
print("Welcome to the Adventure Game, " + player_name + "! Your journey begins here...")

#Use an f-string to display the same message in a more readable format
print(f"Welcome to the Adventure Game, {player_name}! Your journey begins here...")

#Describe the starting of the game
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the 
unknown...
"""

print(starting_area)

# Ask the player for their decission
decission = input("Do you wish to take the path? (yes/no)").lower()

# Responde based on the player's decission
if decission == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example
else:
    print("Confused, you stand still, unsure of what to do.")