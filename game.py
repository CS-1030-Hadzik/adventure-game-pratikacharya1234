# """
# DOCS String
# Adventure Game
# Author: Scott Hadzik
# Version: 1.0
# Description:
# This is a text-based adventure game where the player makes choices
# to navigate through a mysterious forest.
# """



inventory = []

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")


    # Ask for Player Name
    player_name = input("What is your name? ")
    print("Hello, " + player_name + "!")


    # Concatenate Strings to create a personalized message
    print("Welcome to the Adventure Game, " + player_name + "! Your journey begins here...")
    return player_name

def describe_area():
    #Describe the starting of the game
    print( """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the 
    unknown...
    """)

def add_to_inventory(item):
    inventory.append(item)
    print("You pickedup a {item}!")





player_name = welcome_player()
describe_area()


#start of the game
while True:
    print("\nYou see a two path ahead:" )
    print("1. Take the left path into the dark woods.")
    print("2. Take the right path towards the mountain pass.")
    print("3. Wait and observe.")
    print("\t Type 'i' to view inventory.")
    # print("string. abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Ask the player for their decission
    decission = input("What will you do (1,2,3)").lower()

    #loop for invalid input
    if decission not in ["1", "2", "3"]:
        print("Invalid input. Please enter '1', '2', '3'or 'i'.")
            
    # Responde based on the player's decission
    if decission == "i":
        print("Inventory", inventory)
        continue
    if decission == "1":
        print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
        
    elif decission == "2":
        print(f"Bold choice, {player_name}! You take the path towards the mountain pass.")
        add_to_inventory("map")
        
    elif decission == "3":
        print(f"Patient choice, {player_name}! You wait and observe the surroundings.")
        
    # elif decission == "string":
    #     print("Invalid input. Please enter '1', '2', or '3'.")
    #     continue
    else:
        print(f"Cautious choice, {player_name}! You hesitate before taking the path.", decission)

    #Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again != "yes" or "y":
        print("Thank you for playing the Adventure Game!, " + player_name + "!") 
        break #exit the loop and end the game




# # Ask the player for their decission
# decission = input("Do you wish to take the path? (yes/no)").lower()

# #loop for invalid input
# while decission not in ["yes", "no"]:
#     print("Invalid input. Please enter 'yes' or 'no'.")
    
#     # Ask the player for their decission again
#     decission = input("Do you wish to take the path? (yes/no)").lower()

# # Responde based on the player's decission
# if decission == "yes":
#     print(f"Brave choice, {player_name}! You step onto the path and venture forward.")

#     # Code to execute if the player chooses yes
# elif decission == "no":
#     print(player_name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example

#     # Code to execute if the player chooses no
# else:
#     print("Confused, you stand still, unsure of what to do.")