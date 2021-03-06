# Trick or Treat on Spooky Street - Text Adventure Game
# Author: Richard Elphinstone


# List of functions
def show_intro():
    # Print a introduction and the commands.
    print("**********")
    print("███████╗██████╗░██╗░█████╗░██╗░░██╗  ░█████╗░██████╗░  "
          "████████╗██████╗░███████╗░█████╗░███████╗")
    print("╚═██╔══╝██╔══██╗██║██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗  "
          "╚══██╔══╝██╔══██╗██╔════╝██╔══██╗╚══██╔═╝")
    print("░░██║░░░██████╔╝██║██║░░╚═╝█████═╝░  ██║░░██║██████╔╝  "
          "░░░██║░░░██████╔╝█████╗░░███████║░░░██║░░")
    print("░░██║░░░██╔══██╗██║██║░░██╗██╔═██╗░  ██║░░██║██╔══██╗  "
          "░░░██║░░░██╔══██╗██╔══╝░░██╔══██║░░░██║░░")
    print("░░██║░░░██║░░██║██║╚█████╔╝██║░╚██╗  ╚█████╔╝██║░░██║  "
          "░░░██║░░░██║░░██║███████╗██║░░██║░░░██║░░")
    print("░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝  "
          "░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░")
    print("░█████╗░███╗░░██╗  ░██████╗██████╗░░█████╗░░█████╗░██╗░░██╗██"
          "╗░░░██╗")
    print("██╔══██╗████╗░██║  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚█"
          "█╗░██╔╝")
    print("██║░░██║██╔██╗██║  ╚█████╗░██████╔╝██║░░██║██║░░██║█████═╝░░╚"
          "████╔╝░")
    print("██║░░██║██║╚████║  ░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔═██╗░░░"
          "╚██╔╝░░")
    print("╚█████╔╝██║░╚███║  ██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░╚██╗░░"
          "░██║░░░")
    print("░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝░░"
          "░╚═╝░░░")
    print("░██████╗████████╗██████╗░███████╗███████╗████████╗")
    print("██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝")
    print("╚█████╗░░░░██║░░░██████╔╝█████╗░░█████╗░░░░░██║░░░")
    print("░╚═══██╗░░░██║░░░██╔══██╗██╔══╝░░██╔══╝░░░░░██║░░░")
    print("██████╔╝░░░██║░░░██║░░██║███████╗███████╗░░░██║░░░")
    print("╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░")
    input("Press Enter to begin.")
    print("**********")
    print("The homes on Spooky Street each give out one of the best candies in"
          " the whole town.\n"
          "\nThose candies would be:\n*Snacker’s Bar\n*Wreathy’s Peanut Butter"
          " Cups\n*Andromeda Bar\n*Sizzlers\n"
          "*Sour Patch Critters\n*ButterToe Bar\n")
    print("The problem is that a ghost by the name of Mr. Boo haunts\none "
          "random home on Spooky Street every Trick or"
          " Treat on\nHalloween night. Mr. Boo then waits for trick or "
          "treaters\nto come to his haunted house and steals"
          " all their candy.\n")
    print("**********\n")
    print("Your goal is to collect all six types of candy by Trick or Treating"
          " at each house\non Spooky Street while "
          "staying away from the house that Mr. Boo is haunting!\n")
    print("**********")
    print("Move commands: go South, go North, go East, go West")
    print("To Trick or Treat: Type get Candy")
    print("Type exit to quit the game or Help for instruction.")
    print("GOODLUCK!! - - - - \n")

def instructions():
    # Print a list of commands.
    print('\nMove Commands: go South, go North, go East, go West')
    print('To Trick or Treat: Type get Candy')
    print('Type exit to quit the game.\n')

def moving_rooms(direction, room="beginning of Spooky Street", **rooms):
    # Function for moving player from room to room.
    if direction in rooms[room]:  # Check if direction is available.
        print("\nYou just moved to a different location.\n")
        if direction == "North":
            return rooms[room]["North"]
        if direction == "South":
            return rooms[room]["South"]
        if direction == "East":
            return rooms[room]["East"]
        if direction == "West":
            return rooms[room]["West"]
    else:
        print("\nYou can not go that way!\n")  # Invalid direction for room.
        return room

def get_item(command, room = "beginning of Spooky Street", **rooms):
    # Function to find item in house.
    if command in rooms[room]:
        if command == "item":
            value = rooms.get(room).get("item", "None")
            if value != "None":
                print("\n-*-*TRICK OR TREAT!!*-*-\nYou are getting CANDY!\n")
                rooms[room]["item"] = "None"
                return value
            else:
                print("\nYou already got candy from here!")

def check_room(room ="beginning of Spooky Street", **rooms):
    # Function to check if item located in house.
        if room != "beginning of Spooky Street":
            check = rooms.get(room).get("item", "None")
            if check != "None":
                print("WOW! This house has {}!!\n".format(check))

def check_boo(room = "beginning of Spooky Street", **rooms):
    # Function to check for Mr. Boo.
    #for room in rooms:
        check = rooms.get(room).get("item")
        if check == "Mr. BOO":
            print("Mr Boo got you!")
            return check

def show_status(inventory, current_room = 'beginning of Spooky Street', **rooms):
    # Current player location.
    print("##########\n")
    print("You are currently at {}\n".format(current_room))
    check_room(current_room, **rooms)  # Check for candy available for player to get.
    print("Inventory: {}\n".format(inventory))
    print("##########\n")

def you_lost():
    # Will display when player finds Mr. Boo.
    print("███╗░░░███╗██████╗░░░░  ██████╗░░█████╗░░█████╗░  ░████"
          "██╗░░█████╗░████████╗")
    print("████╗░████║██╔══██╗░░░  ██╔══██╗██╔══██╗██╔══██╗  ██╔══"
          "══╝░██╔══██╗╚══██╔══╝")
    print("██╔████╔██║██████╔╝░░░  ██████╦╝██║░░██║██║░░██║  ██║░░"
          "██╗░██║░░██║░░░██║░░░")
    print("██║╚██╔╝██║██╔══██╗░░░  ██╔══██╗██║░░██║██║░░██║  ██║░░"
          "╚██╗██║░░██║░░░██║░░░")
    print("██║░╚═╝░██║██║░░██║██╗  ██████╦╝╚█████╔╝╚█████╔╝  ╚████"
          "██╔╝╚█████╔╝░░░██║░░░")
    print("╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝  ╚═════╝░░╚════╝░░╚════╝░  ░╚═══"
          "══╝░░╚════╝░░░░╚═╝░░░")
    print("██╗░░░██╗░█████╗░██╗░░░██╗██╗")
    print("╚██╗░██╔╝██╔══██╗██║░░░██║██║")
    print("░╚████╔╝░██║░░██║██║░░░██║██║")
    print("░░╚██╔╝░░██║░░██║██║░░░██║╚═╝")
    print("░░░██║░░░╚█████╔╝╚██████╔╝██╗")
    print("░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝")
    input("Sorry you lost. Press Enter to continue.")  # Pause to read.

def you_won():
    # Will display when player collects all six candies.
    print("██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗")
    print("╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║")
    print("░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║")
    print("░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║")
    print("░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║")
    print("░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝")
    input("CONGRATULATIONS!!!\n Press Enter to continue.")  # Pause to read.

def main():
    # Main game loop.
    rooms = {"beginning of Spooky Street": {"East": "Mr. Kneebly's House",
                                            "West": "The Dursley's House"},
             "Mr. Kneebly's House": {"North": "The Hyde's House",
                                     "West": "beginning of Spooky Street",
                                     "item": "Sizzlers"},
             "The Hyde's House": {'West': "The McFadden's House",
                                  "South": "Mr. Kneebly's House",
                                  "item": "Wreathy's Peanut Butter Cups"},
             "The McFadden's House": {"East": "The Hyde's House",
                                      "West": "The Crane's House",
                                      "item": "Mr. BOO"},
             "The Crane's House": {"North": "The Grave Yard",
                                   "East": "The McFadden's House",
                                   "South": "The Dursley's House",
                                   "item": "A Snacker's Bar"},
             "The Dursley's House": {"North": "The Crane's House",
                                     "East": "beginning of Spooky Street",
                                     "item": "A Andromeda Bar"},
             "The Grave Yard": {"East": "Old Man Smither's Creepy Cabin",
                                "South": "The Crane's House",
                                "item": "A ButterToe Bar"},
             "Old Man Smither's Creepy Cabin": {"West": "The Grave Yard",
                                                "item": "Sour Patch Critters"}
             }

    current_room = "beginning of Spooky Street"
    inventory = []  # List of candies.
    while current_room != "Exit":
        show_status(inventory, current_room, **rooms)
        check = check_boo(current_room, **rooms)
        if check == "Mr. BOO":  # Check for losing condition.
            you_lost()
            break
        elif len(inventory) >= 6:  # Check for winning condition.
            you_won()
            break
        else:  # Player inputs choice of command.
            user_input = input("Type Command\nOr type exit to quit game.\n")
            if user_input == "exit":  # Will exit game loop for player.
                current_room = "Exit"
            elif user_input == "go North":
                current_room = moving_rooms("North", current_room, **rooms)
            elif user_input == "go South":
                current_room = moving_rooms("South", current_room, **rooms)
            elif user_input == "go East":
                current_room = moving_rooms("East", current_room, **rooms)
            elif user_input == "go West":
                current_room = moving_rooms("West", current_room, **rooms)
            elif user_input == "get Candy":
                candy = get_item("item", current_room, **rooms)
                if candy is not None:
                    if inventory.count(candy) <= 0:  # Prevention of duplicate.
                        inventory.append(candy)  # Adds candy to inventory.
            elif user_input == "Help":
                instructions()
            else:
                print("\nThat does not make sense. Please Try a Command."
                      "\nType Help for Instructions\n")  # Invalid command.

def end_game():
    # Game is exiting. Goodbye message.
    print("                 ██████████████")
    print("               ██              ████")
    print("              ██                    ██")
    print("              ██                     ██")
    print("            ██    ████      ████      ██")
    print("            ██  ██▓▓██      ██▓▓██    ██")
    print("          ██    ████          ████    ██")
    print("          ██                           ██")
    print("          ████                      ██  ██")
    print("          ██  ████              ████    ██")
    print("          ██  ██▓▓██  ██  ██  ██▓▓██    ██")
    print("          ██    ██▒▒██▓▓██▓▓██▓▓██      ██")
    print("          ██      ██  ██  ██  ██        ██")
    print("          ██                            ██")
    print("    ██████                  ██████      ██")
    print("  ██            ░░░░░░    ██            ██ ")
    print("██        ██    ░░░░░░░░██        ░░    ██              ██")
    print("██      ████    ░░░░░░░░██      ██░░      ██            ██")
    print("██    ██  ██    ░░░░░░░░██    ██░░░░░░    ██          ██  ██")
    print("██    ██  ██    ░░░░░░░░██    ██░░░░░░    ██          ██  ██")
    print("██    ██  ██      ░░░░░░██    ██░░░░░░    ██      ████    ██")
    print("  ████      ██    ░░░░░░░░████░░░░░░░░      ██████      ██")
    print("            ██      ░░░░░░░░░░░░░░░░░░░░            ░░  ██")
    print("              ██    ░░░░░░░░░░░░░░░░░░░░░░      ░░░░    ██")
    print("              ██      ░░░░░░░░░░░░░░░░░░░░░░░░░░      ██")
    print("                ██      ░░░░░░░░░░░░░░░░░░░░        ██")
    print("                  ██        ░░░░                ████")
    print("                    ██▓▓            ████    ████")
    print("                        ████      ██    ████")
    print("                            ██████ ")
    response = input("\n\nThank you for playing!\n"
          "Want to play again? Type replay."
          "If not press Enter."
          "\nGood Bye!")
    if response == "replay":
        return "yes"  # restart game.
    else:
        return "no"  # Player has quit game.

# Game set-up.
value = "yes"
while value != "no":
    show_intro()
    main()
    value = end_game()
