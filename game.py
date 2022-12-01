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
# Game flow: describe place, *display choices, *decorate choices if there is a challenge, save choices in a list/dict
#                            ^if choice is a transit station: display choices of station


import random
import json


START = (9, 2)
WATER = ((0, 0), (0, 1), (0, 2), (0, 3), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2), (1, 3), (1, 6), (1, 7), (1, 8), (1, 9),
         (2, 0), (2, 1), (2, 2), (5, 0), (6, 0), (6, 1), (7, 0), (7, 1), (7, 2), (8, 0), (8, 3), (9, 0), (9, 4), (9, 5),
         (9, 6), (9, 7), (9, 8), (9, 9))
OAKRIDGE = ((5, 3), (5, 4), (5, 5), (5, 6), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 3), (7, 4), (7, 5), (7, 6))
UBC = ((3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 1), (5, 2))
DOWNTOWN = ((1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6))
LOCATIONS = ((0, 7), (1, 4), (1, 5), (2, 5), (2, 3), (3, 2), (3, 3), (3, 4), (4, 6), (5, 6), (6, 4), (6, 6), (6, 8),
             (8, 4), (9, 2), (9, 3))
CHURCH = ()
HOSPITAL = ()
CONSUMABLES = ()




# do we need a make_board if we're using a static map?
def display_title():
    """
    Display title
    """
    with open("dialogue.txt") as file_object:
        lines = file_object.readlines()
        print("".join(lines[1:16]))


def display_prologue():
    with open("dialogue.txt") as file_object:
        lines = file_object.readlines()
        print("".join(lines[17:19]))


def make_board(rows, columns):
    """
    Create all possible X and Y positions on a grid.

    :param rows:
    :param columns:
    :postcondition:
    :return:

    >>> make_board(3, 3)
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    board = []
    for position_x in range(rows):
        for position_y in range(columns):
            board.append((position_x, position_y))
    return board



def display_board(character):
    # dynamically displays a board depending on character["position"]


def pick_spells(character):
    # name: [target, damage, cost]
    if character["level"] == 1:
        spells_dict = {"Burn": ["enemy", 10, 10],
                       # reckless is RNG damage, should clarify with print statement or description
                       "Reckless": ["enemy", random.randint(0, 20), 12],
                       "Heal": ["player", 15, 10]}
        for option_num, spell in enumerate(spells_dict):
            print(f"{option_num}: {spell}")
        selection = int(input("Select a spell: "))
        if selection == 0:
            chosen_spell = "Burn"
        elif selection == 1:
            chosen_spell = "Reckless"
        else:
            chosen_spell = "Heal"
        print(f"You have selected {chosen_spell}")
        character["spells"][chosen_spell] = spells_dict[chosen_spell]
    return character


def make_character(name):
    # on character creation
    character = {"name": name,
                 "level": 1,
                 "current_exp": 0,
                 "exp_needed": 100,
                 "position": START,
                 "attack": 1,
                 "defense": 1,
                 "speed": 2,
                 "spells": dict()}
    pick_spells(character)
    return character


def exp_to_level_up(character):
    # detect character level, detects exp needed to level up
    # returns an integer representing exp needed to level up
    if character["level"] == 1:
        exp_needed = 100 - character["current_exp"]
        return exp_needed
    if character["level"] == 2:
        exp_needed = 200 - character["current_exp"]
        return exp_needed


def level_up(character):
    # plays whenever character levels up
    # instead of printing "has levelled up", can do ASCII art
    print(character["name"], "has leveled up!")
    # these are the stats that go up
    character["level"] += 1
    # these stats reset back to 0 or default for level
    character["current_exp"] = 0
    character["exp_needed"] = exp_to_level_up(character)
    return character


def validate_move(board, character, direction):
    # checks out what's in next position
    x_position, y_position = character["position"]
    if direction == "W":
        new_position = (x_position, y_position + 1)
    elif direction == "A":
        new_position = (x_position - 1, y_position)
    elif direction == "S":
        new_position = (x_position, y_position - 1)
    else:
        new_position = (x_position + 1, y_position)

    # if the next position is out of bounds, return False
    if (new_position in WATER) or\
            (new_position in UBC and character["level"] < 2) or\
            (new_position in DOWNTOWN and character["level"] < 3):
        return False
    # else return True
    else:
        return True


def display_dialogue(position):
    with open("dialogue.txt") as file_object:
        lines = file_object.readlines()
        # bunch of if statements for each location
        if position == (0, 7):
            print("".join(lines[:]))
        if position == (1, 4):
            print("".join(lines[:]))
        if position == (1, 5):
            print("".join(lines[:]))
        if position == (2, 3):
            print("".join(lines[:]))
        if position == (2, 5):
            print("".join(lines[:]))
        if position == (3, 0):
            print("".join(lines[:]))
        if position == (3, 2):
            print("".join(lines[:]))
        if position == (3, 3):
            print("".join(lines[:]))
        if position == (3, 4):
            print("".join(lines[:]))
        if position == (3, 6):
            print("".join(lines[:]))
        if position == (4, 6):
            print("".join(lines[:]))
        if position == (5, 6):
            print("".join(lines[:]))
        if position == (6, 4):
            print("".join(lines[:]))
        if position == (6, 6):
            print("".join(lines[:]))
        if position == (6, 8):
            print("".join(lines[:]))
        if position == (8, 4):
            print("".join(lines[:]))
        if position == (9, 2):
            print("".join(lines[:]))
        if position == (9, 3):
            print("".join(lines[:]))



def display_transit(line):
    with open("transit.json") as file_object:
        lines = json.load(file_object)
        for station, name in enumerate(lines[line]):
            print(station, name)


def display_choices(position):
    choices = []
    with open("locations.json") as file_object:
        locations = json.load(file_object)
        for location_number, name in enumerate(locations[position]):
            print(location_number, name)
            choices.append(name)
    return choices

def check_for_challenges():
    pass



def describe_current_location(character):
    print(f"You are at {str(character['position'])}")
    choices = []
    if character["position"] in LOCATIONS:
        display_dialogue(character['position'])
        location_choices = display_choices(str(character['position']))
        choices += location_choices
        there_is_a_challenge = check_for_challenges()
        if there_is_a_challenge:
            execute_challenge_protocol(character)
    return #choices


def move(character):
    direction = input("Move by entering W, A, S, or D")
    x_position, y_position = character["position"]
    if direction == "W".lower:
        # what is board here?
        if validate_move(board, character, "W"):
            character["position"] = (x_position, y_position + 1)
        else:
            print("Invalid move.")
        # x += 1
    if direction == "A".lower:
        if validate_move(board, character, "A"):
            character["position"] = (x_position - 1, y_position)
        else:
            print("Invalid move.")
        # y -= 1
    if direction == "S".lower:
        if validate_move(board, character, "S"):
            character["position"] = (x_position, y_position - 1)
        else:
            print("Invalid move.")
        # x -= 1
    if direction == "D".lower:
        if validate_move(board, character, "D"):
            character["position"] = (x_position + 1, y_position)
        else:
            print("Invalid move.")
        # y += 1
    # doesn't need return I think


def start_game(): # called from main
    rows = 10
    columns = 10
    # done
    board = make_board(rows, columns)
    # done but could be adjusted
    display_title()
    character = make_character(input("Enter your name: "))
    display_prologue()
    achieved_goal = False
    while not achieved_goal:
        # Tell the user where they are
        describe_current_location(character)
        # Asks user for move input, validates input, moves. If invalid, tells user.
        move()
        if character_has_leveled():
            execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
    # Print end of game stuff like congratulations or sorry you died



def main():
    """
    Runs the program.
    """
    start_game()


if __name__ == '__main__':
    main()