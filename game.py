"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""
import random


# do we need a make_board if we're using a static map?
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



def display_board():


def pick_spells(character):
    # name: [target, damage, cost]
    if character["level"] == 1:
        spells_dict = {"Burn": ["enemy", 10, 10],
                       "Reckless": ["enemy", random.randint(0, 20), 12],
                       "Heal": ["player", 15, 10]}
        for option_num, spell in enumerate(spells_dict):
            print(f"{option_num}: {spell}")
        selection = input("Select a spell: ")
        if selection == 0:
            chosen_spell = "Burn"
        elif selection == 1:
            chosen_spell = "Reckless"
        else:
            chosen_spell = "Heal"
        print(f"You have selected {chosen_spell}")
        character["spells"] = character["spells"].append(spells_dict[chosen_spell])
    return character


def make_character(name):
    # on character creation
    character = {"name": name,
                 "level": 1,
                 "current_exp": 0,
                 "exp_needed": 100,
                 "attack": 1,
                 "defense": 1,
                 "speed": 2,
                 "spells": []}
    # could add customization, ex. letting users decide stats at the beginning with inputs
    pick_spells(character)
    move()
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


def move(north, east, west, south):


def describe_current_location(board, character):
        print(f"To your north is {}, to your east is {}, to your south is {}, to your west is {}.")

def get_user_choice():


def start_game(): # called from main
    rows = 10
    columns = 10
    # done
    board = make_board(rows, columns)
    # done but could be adjusted
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        # // Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice( )
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
            if character_has_leveled():
                execute_glow_up_protocol()
                achieved_goal = check_if_goal_attained(board, character)
        else:
            # // Tell the user they can’t go in that direction
            # // Print end of game stuff like congratulations or sorry you died


def main():
    """
    Runs the program.
    """
    start_game()


if __name__ == '__main__':
    main()