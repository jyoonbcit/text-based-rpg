"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""

def make_character(name):
    character = {"name": name, "level": 1, "current_exp": 0, "exp_needed": 100}
    return character


def exp_to_level_up(character):
    if character["level"] == 1:
        character["exp_needed"] = 100
        return 100
    if character["level"] == 2:
        character["exp_needed"] = 200
        return 200


def game(): # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
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


if __name__ == '__main__':
    main()