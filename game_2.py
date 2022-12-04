"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""
# TO-DO-LIST
# Add descriptions to the board positions in dialogue.txt
# Implement pick_spells for level 2, 3, etc
# Get display board to display
# Assign START (global constant) to the beginning point of our map
# Add ASCII art
# For myself (Jihoon): Check if return statements are necessary for variable adjustments, eg. move fn


import random
import battle_2
import transit


START = (9, 2)
BOSS = ((1, 5), (2, 5), (3, 0), (6, 4))


def display_title():
    """
    Display title.
    """
    with open("dialogue.txt", encoding='utf-8') as file_object:
        lines = file_object.readlines()
        print("".join(lines[1:16]))


def display_prologue():
    """
    Display prologue.
    """
    with open("dialogue.txt", encoding='utf-8') as file_object:
        lines = file_object.readlines()
        print("".join(lines[17:23]))


def make_board(rows, columns):
    """
    Create all possible X and Y positions on a grid.

    :param rows: integer
    :param columns: integer
    :postcondition: create a 2D list of tuples with specified rows and specified columns
    :return: list of tuples

    >>> make_board(3, 3)
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    board = []
    for position_x in range(rows):
        for position_y in range(columns):
            board.append((position_x, position_y))
    return board


def display_board(character):
    """

    :param character:
    :return:
    """
    # placeholder display
    print(character["position"])


def pick_spells(character):
    """
    Gives the specified character a spell depending on their level and choice.

    :param character: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character["spells"] changes or remains the same
    :return: dictionary
    """
    # name: [target, damage, cost]
    if character["level"] == 5:
        spells_dict = {"Burn": {"target": "enemy", "strength": 25, "cost": 10},
                       # reckless is RNG damage, should clarify with print statement or description
                       "Reckless": {"target": "enemy", "strength": random.randint(0, 50), "cost": 12},
                       "Heal": {"target": "player", "strength": 15, "cost": 10}}
        for option_num, spell in enumerate(spells_dict):
            print(f"{option_num}: {spell}")
        selection = int(input("Select a spell to learn: "))
        if selection == 0:
            chosen_spell = "Burn"
        elif selection == 1:
            chosen_spell = "Reckless"
        else:
            chosen_spell = "Heal"
        print(f"You have learnt {chosen_spell}")
        character["spells"][chosen_spell] = spells_dict[chosen_spell]
    return character


def make_character(name):
    """
    Create a character from scratch.

    :param name: string
    :postcondition: create a character with a specified name
    :return: dictionary
    """
    # on character creation
    character = {"name": name,
                 "level": 1,
                 "current_exp": 0,
                 "exp_needed": 100,
                 "position": START,
                 "health": 100,
                 "max_health": 100,
                 "mana": 100,
                 "max_mana": 100,
                 "attack": 10,
                 "defense": 10,
                 "speed": 2,
                 "spells": dict(),
                 "win": False}
    return character


def exp_to_level_up(character):
    """
    Calculate the experience a specified character

    :param character: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character is unchanged
    :return: integer
    """
    # detect character level, detects exp needed to level up
    # returns an integer representing exp needed to level up
    if character["level"] == 1:
        exp_needed = 100 - character["current_exp"]
        return exp_needed
    if character["level"] == 2 or character["level"] == 3:
        exp_needed = 200 - character["current_exp"]
        return exp_needed
    if character["level"] == 4 or character["level"] == 5:
        exp_needed = 250 - character["current_exp"]
        return exp_needed
    if character["level"] > 5:
        return 300 - character["current_exp"]


def level_up(character):
    """
    Increase a specified character's level.

    :param character: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character["level"] increases by 1
    :postcondition: character["current_exp"] becomes 0
    :postcondition: character["exp_needed"] increases or remains the same
    :return: dictionary
    """
    # plays whenever character levels up
    # instead of printing "has levelled up", can do ASCII art
    character["level"] += 1
    print(f"You've levelled up! You are now level {character['level']}.\n")
    # these are the stats that go up
    # these stats reset back to 0 or default for level
    character["current_exp"] = 0
    character["exp_needed"] = exp_to_level_up(character)
    return character


def validate_move(character, direction, board):
    """
    Validate whether a move is possible or not.

    :param character: dictionary
    :param direction: string
    :param board: list of tuples
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character is unchanged
    :postcondition: direction is unchanged
    :postcondition: board is unchanged
    :return: False if move is not valid, else True
    """
    # checks out what's in next position
    x_position, y_position = character["position"]
    if direction == "W":
        new_position = (x_position, y_position - 1)
    elif direction == "A":
        new_position = (x_position - 1, y_position)
    elif direction == "S":
        new_position = (x_position, y_position + 1)
    else:
        new_position = (x_position + 1, y_position)
    # if the next position is out of bounds, return False
    if new_position not in board:
        return False
    # else return True
    else:
        return True


def display_dialogue(position):
    """
    Display a specific dialogue depending on a specified position.

    :param position: tuple
    :postcondition: print a specific message based on position
    :return: none
    """
    with open("dialogue.txt", encoding='utf-8') as file_object:
        lines = file_object.readlines()
        # bunch of if statements for each location
        if position == (0, 7):
            print("".join(lines[46:50]))
        if position == (1, 4):
            print("".join(lines[51:57]))
        if position == (1, 5):
            print("".join(lines[58:63]))
        if position == (2, 3):
            print("".join(lines[64:75]))
        if position == (2, 5):
            print("".join(lines[76:83]))
        if position == (3, 0):
            print("".join(lines[84:86]))
        if position == (3, 2):
            print("".join(lines[87:89]))
        if position == (3, 3):
            print("".join(lines[90:92]))
        if position == (3, 4):
            print("".join(lines[93:96]))
        if position == (3, 6):
            print("".join(lines[97:100]))
        if position == (4, 6):
            print("".join(lines[101:104]))
        if position == (5, 6):
            print("".join(lines[105:108]))
        if position == (6, 4):
            print("".join(lines[109:112]))
        if position == (6, 6):
            print("".join(lines[113:118]))
        if position == (6, 8):
            print("".join(lines[119:125]))
        if position == (8, 4):
            print("".join(lines[126:130]))
        if position == (9, 2) or (9, 3):
            print("".join(lines[131:136]))


def describe_current_location(character, board):
    """
    Display details about a specified character's position.

    :param character: dictionary
    :param board: list of tuples
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character is unchanged
    :return: none
    """
    print(f"You are at {str(character['position'])}")
    if character["position"] in board:
        display_dialogue(character['position'])


def move(character, board):
    """
    Move character one tile towards a specified direction.

    :param character: dictionary
    :param board: list of tuples
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character["position"] is changed or remains the same
    :return: none
    """
    direction = input("Move by entering W, A, S, or D: ")
    x_position, y_position = character["position"]
    if direction == "w" and validate_move(character, "W", board):
        character["position"] = (x_position, y_position + 1)
        print(f"You are at {character['position']}\n")
        is_encounter, enemy = battle_2.encounter_enemy(character, character["position"])
        if is_encounter and enemy is not None:
            battle_2.engage_battle(character, enemy)
    # y -= 1
    elif direction == "a" and validate_move(character, "A", board):
        character["position"] = (x_position - 1, y_position)
        print(f"You are at {character['position']}\n")
        is_encounter, enemy = battle_2.encounter_enemy(character, character["position"])
        if is_encounter and enemy is not None:
            battle_2.engage_battle(character, enemy)
    # x -= 1
    elif direction == "s" and validate_move(character, "S", board):
        character["position"] = (x_position, y_position - 1)
        print(f"You are at {character['position']}\n")
        is_encounter, enemy = battle_2.encounter_enemy(character, character["position"])
        if is_encounter and enemy is not None:
            battle_2.engage_battle(character, enemy)
    # y += 1
    elif direction == "d" and validate_move(character, "D", board):
        character["position"] = (x_position + 1, y_position)
        print(f"You are at {character['position']}\n")
        is_encounter, enemy = battle_2.encounter_enemy(character, character["position"])
        if is_encounter and enemy is not None:
            battle_2.engage_battle(character, enemy)
    # x += 1
    else:
        print("Invalid move.\n")


def start_game():
    """
    Starts the game.
    """
    board = make_board(10, 10)
    display_title()
    character = make_character(input("Enter your name: "))
    display_prologue()
    while not character["win"]:
        # Tell the user where they are
        describe_current_location(character, board)
        print(f"{character['name']}:"
              f" {character['health']}/{character['max_health']} HP"
              f" | {character['mana']}/{character['max_mana']} MP"
              f" | {character['exp_needed']} EXP to next level\n")
        if transit.transit_available(character):
            if transit.you_want_a_ride():
                transit.ride_transit(character)
            else:
                # Asks user for move input, validates input, moves. If invalid, tells user.
                move(character, board)
        # Asks user for move input, validates input, moves. If invalid, tells user.
        move(character, board)
    print("Winner winner chicken dinner!")


def main():
    """
    Runs the program.
    """
    start_game()


if __name__ == '__main__':
    main()
