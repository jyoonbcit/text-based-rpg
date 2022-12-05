"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""
import random
import battle
import transit
import itertools


START = (9, 2)
LOCATIONS = ((0, 7), (1, 4), (1, 5), (2, 5), (2, 3), (3, 2), (3, 3), (3, 4), (4, 6), (5, 6), (6, 4), (6, 6), (6, 8),
             (8, 4), (9, 2), (9, 3))
WATER = ((0, 0), (0, 1), (0, 2), (0, 3), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2), (1, 3), (1, 6), (1, 7), (1, 8), (1, 9),
         (2, 0), (2, 1), (2, 2), (5, 0), (6, 0), (6, 1), (7, 0), (7, 1), (7, 2), (8, 0), (8, 3), (9, 0), (9, 4), (9, 5),
         (9, 6), (9, 7), (9, 8), (9, 9))
BOSS = ((1, 5), (2, 5), (3, 0), (6, 4))


def display_title():
    """
    Display title.
    """
    with open("dialogue.txt", encoding='utf-8') as file_object:
        lines = file_object.readlines()
        print("".join(lines[0:16]))


def display_prologue():
    """
    Display prologue.
    """
    with open("dialogue.txt", encoding='utf-8') as file_object:
        lines = file_object.readlines()
        print("".join(lines[16:23]))


def make_board(sides):
    """
    Create a square board with specified sides.

    :param sides: integer
    :postcondition: create a 2D list of tuples with the same amount of rows and columns
    :return: list of tuples

    >>> make_board(3)
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    board = (list(itertools.product(range(sides), repeat=2)))
    return board


def display_board(character):
    """
    Print a map of the board

    :param character: a dictionary of stats (we want the position)
    """
    # placeholder display
    sud = ""
    for row in range(0, 10):
        sud += "" if row == 0 else "\n"
        for column in range(0, 10):
            current_position = (row, column)
            if current_position == character["position"]:
                sud += "[#]"
            elif current_position in WATER:
                sud += "(~)"
            else:
                sud += "[^]"
    print(sud)


def random_damage():
    """
    Pick a random amount of damage between 0, 40, and 80

    :return: int
    """
    return random.choice((0, 40, 80))


def pick_spells(character):
    """
    Gives the specified character a spell depending on their level and choice.

    :param character: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character["spells"] changes or remains the same
    :return: dictionary
    """
    # name: [target, damage, cost]
    if character["level"] == 2:
        print("\nYou can now pick a spell.")
        spells_dict = {"Burn": {"target": "enemy", "strength": 25, "cost": 10},
                       "Heal": {"target": "player", "strength": 15, "cost": 10}}
        for option_num, spell in enumerate(spells_dict):
            print(f"{option_num}: {spell}")
        selection = int(input("Select a spell to learn: "))
        if selection == 0:
            chosen_spell = "Burn"
        else:
            chosen_spell = "Heal"
        print(f"You have learnt {chosen_spell}")
        character["spells"][chosen_spell] = spells_dict[chosen_spell]
    if character["level"] == 3:
        print("\nYou can now pick a spell.")
        spells_dict = {"Incinerate": {"target": "enemy", "strength": 40, "cost": 25},
                       "Reckless 2.0": {"target": "enemy", "strength": random_damage(), "cost": 40}}
        for option_num, spell in enumerate(spells_dict):
            print(f"{option_num}: {spell}")
        selection = int(input("Select a spell to learn: "))
        if selection == 0:
            chosen_spell = "Incinerate"
        else:
            chosen_spell = "Reckless 2.0"
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
                 "health": 50,
                 "max_health": 50,
                 "mana": 50,
                 "max_mana": 50,
                 "attack": 10,
                 "defense": 0,
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
        exp_needed = 150 - character["current_exp"]
        return exp_needed


def level_up(character):
    """
    Increase a specified character's level.

    :param character: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character["level"] increases by 1
    :postcondition: character["current_exp"] becomes 0
    :postcondition: character["exp_needed"] increases or remains the same
    :postcondition: character["max_health"] increases
    :postcondition: character["health"] increases
    :postcondition: character["attack"] increases
    :postcondition: character["defense"] increases
    :postcondition: character["max_mana"] increases
    :postcondition: character["mana"] increases
    :return: dictionary
    """
    # plays whenever character levels up
    character["level"] += 1
    print(f"\nYou have levelled up! You are now level {character['level']}.")
    character["max_health"] += 10
    character["health"] = character["max_health"]
    character["attack"] += 5
    character["defense"] += 3
    character["max_mana"] += 10
    character["mana"] = character["max_mana"]
    pick_spells(character)

    print(f"You've levelled up! You are now level {character['level']}.\n")
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

    >>> test = make_character("Test One")
    >>> validate_move(test, "S", make_board(10))
    False
    >>> test = make_character("Test Two")
    >>> validate_move(test, "D", make_board(10))
    True
    """
    # checks out what's in next position
    y_position, x_position = character["position"]
    if direction == "W":
        new_position = (y_position - 1, x_position)
    elif direction == "A":
        new_position = (y_position, x_position - 1)
    elif direction == "S":
        new_position = (y_position + 1, x_position)
    elif direction == "D":
        new_position = (y_position, x_position + 1)
    else:
        return False
    # if the next position is out of bounds, return False
    if new_position not in board:
        return False
    elif new_position in WATER:
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
            print("".join(lines[45:50]))
        if position == (1, 4):
            print("".join(lines[50:57]))
        if position == (1, 5):
            print("".join(lines[57:63]))
        if position == (2, 3):
            print("".join(lines[63:75]))
        if position == (2, 5):
            print("".join(lines[75:83]))
        if position == (3, 0):
            print("".join(lines[83:86]))
        if position == (3, 2):
            print("".join(lines[86:89]))
        if position == (3, 3):
            print("".join(lines[89:92]))
        if position == (3, 4):
            print("".join(lines[92:96]))
        if position == (3, 6):
            print("".join(lines[96:100]))
        if position == (4, 6):
            print("".join(lines[100:104]))
        if position == (5, 6):
            print("".join(lines[104:108]))
        if position == (6, 4):
            print("".join(lines[108:112]))
        if position == (6, 6):
            print("".join(lines[112:118]))
        if position == (6, 8):
            print("".join(lines[118:125]))
        if position == (8, 4):
            print("".join(lines[125:130]))
        if position == (9, 2) or position == (9, 3):
            print("".join(lines[130:136]))
        else:
            print("")


def describe_current_location(character):
    """
    Display details about a specified character's position.

    :param character: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character is unchanged
    :return: none
    """
    print(f"You are at {str(character['position'])}")
    if character["position"] in LOCATIONS:
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
    print("Hit q to quit")
    current_situation(character)
    direction = input("Move by entering W, A, S, or D: ")
    y_position, x_position = character["position"]
    if direction == "w" and validate_move(character, "W", board):
        character["position"] = (y_position - 1, x_position)
        print(f"You are at {character['position']}\n")
    elif direction == "a" and validate_move(character, "A", board):
        character["position"] = (y_position, x_position - 1)
        print(f"You are at {character['position']}\n")
    elif direction == "s" and validate_move(character, "S", board):
        character["position"] = (y_position + 1, x_position)
        print(f"You are at {character['position']}\n")
    elif direction == "d" and validate_move(character, "D", board):
        character["position"] = (y_position, x_position + 1)
        print(f"You are at {character['position']}\n")
    elif direction == "q":
        print("You have quit the game.")
        quit()
    else:
        print("Invalid move.\n")


def current_situation(character):
    """
    Explain the current situation of specified character.

    :param character: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :postcondition: character is unchanged
    :return: none
    """
    describe_current_location(character)
    display_board(character)
    print(f"{character['name']}:"
          f" {character['health']}/{character['max_health']} HP"
          f" | {character['mana']}/{character['max_mana']} MP"
          f" | {character['exp_needed']} EXP to next level\n")


def start_game():
    """
    Starts the game.
    """
    board = make_board(10)
    display_title()
    character = make_character(input("Enter your name: "))
    display_prologue()
    while not character["win"]:
        # Tell the user where they are
        current_situation(character)
        is_encounter, enemy = battle.encounter_enemy(character, character["position"])
        if is_encounter and enemy is not None:
            battle.engage_battle(character, enemy)
        if transit.transit_available(character):
            if transit.you_want_a_ride():
                transit.ride_transit(character)
                current_situation(character)
                is_encounter, enemy = battle.encounter_enemy(character, character["position"])
                if is_encounter and enemy is not None:
                    battle.engage_battle(character, enemy)
        # Asks user for move input, validates input, moves. If invalid, tells user.
        move(character, board)
    with open("dialogue.txt", encoding='utf-8') as file_object:
        lines = file_object.readlines()
        print("".join(lines[136:148]))


def main():
    """
    Runs the program.
    """
    start_game()


if __name__ == '__main__':
    main()
