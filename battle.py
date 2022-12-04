"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""
import random
import game


def make_enemy(name, health, attack, defense, exp_value, speed=1, is_boss=False):
    """
    Create an enemy in the form of a dictionary.

    :param name: string
    :param health: integer
    :param attack: integer
    :param defense: integer
    :param exp_value: integer
    :param speed: integer
    :param is_boss: boolean
    :precondition: attack is greater than or equal to 0
    :precondition: defense is greater than or equal to 0
    :precondition: exp_value is greater than or equal to 0
    :precondition: speed is greater than or equal to 1
    :postcondition: enemy dictionary is created with specified keys and values
    :return: dictionary that contains keys and values representing fields of an enemy entity

    >>> make_enemy("Test", 1, 1, 1, 1)
    {'name': 'Test', 'health': 1, 'attack': 1, 'defense': 1, 'speed': 1, 'exp_value': 1, 'run': False, 'is_boss': False}
    """
    enemy = {"name": name,
             "health": health,
             "attack": attack,
             "defense": defense,
             "speed": speed,
             "exp_value": exp_value,
             "run": False,
             "is_boss": is_boss}
    return enemy


def engage_boss():
    """
    Return True if you say yes, False if you say no.

    :return: True if yes, False if no
    """
    choices = ["Yes", "No"]
    decisions = {choice: name for choice, name in enumerate(choices, 1)}
    print("You sense a strong presence. Do you want to engage the boss of this area?")
    for choice, name in enumerate(choices, 1):
        print(choice, name)
    decision = int(input("ENTER number:"))
    while decision not in decisions.keys():
        print("Invalid input. Try again")
        print("You sense a strong presence. Do you want to engage the boss of this area?")
        for choice, name in enumerate(choices, 1):
            print(choice, name)
        decision = int(input("ENTER number:"))
    choice = decisions[decision]
    if choice == "Yes":
        return True
    else:
        return False


def encounter_enemy(character, location):
    """
    Determine if a specified character has encountered an enemy at a specified location.

    :param character: dictionary
    :param location: tuple
    :precondition: character must be a dictionary containing the fields of a character dictionary
    """
    if location not in game.BOSS and location not in game.START:
        enemy = make_enemy(random.choice(["Bandit", "Wolf", "Demon"]),
                           # health
                           character["level"] * random.randint(5, 10),
                           # attack
                           character["level"] * random.randint(5, 10),
                           # defense
                           character["level"] * random.randint(0, 5),
                           # exp given
                           character["level"] * 15
                           )
        print(f"You have encountered {enemy['name']}!")
        return True, enemy
    elif location in game.BOSS:
        if engage_boss():
            enemy = make_enemy("Boss", 1000, 100, 100, 0, speed=3, is_boss=True)
            return True, enemy
        else:
            return False, None
    else:
        return False, None


def enemy_turn(character, enemy):
    """
    Determine the damage a specified character will take from a specified enemy.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :precondition: enemy must be a dictionary containing the fields of an enemy dictionary
    :postcondition: character["health"] is reduced or remains the same
    :return: none
    """
    if character["defense"] > enemy["attack"]:
        print(f"You have taken 0 damage from {enemy['name']}.")
    else:
        character["health"] -= enemy["attack"]
        print(f"You have taken {enemy['attack'] - character['defense']} damage from {enemy['name']}.\n"
              f"You have {character['health']} HP and {character['mana']} mana.")


def battle_options(character, enemy):
    """
    Display to the player what options they can take in combat.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :precondition: enemy must be a dictionary containing the fields of an enemy dictionary
    :postcondition: character["health"] is increased or remains the same
    :postcondition: character["mana"] is decreased or remains the same
    :postcondition: enemy["health"] is decreased or remains the same
    :postcondition: enemy["run"] becomes True or remains the same
    :return: none
    """
    options = ["Attack", "Skill", "Run"]
    print("Make your decision:")
    for decision, option in enumerate(options, 0):
        print(decision, option)
    choice = input()
    if choice != "0" and choice != "1" and choice != "2":
        print(f"{character['name']} does not understand your command!\nOh no, you've been caught off-guard!")
    if choice == "0":
        if character["attack"] - enemy["defense"] >= 0:
            before = enemy["health"]
            enemy["health"] -= character["attack"] - enemy["defense"]
            print(f"You have dealt {before - enemy['health']} damage!\n"
                  f"The enemy has {enemy['health']} HP.")
        else:
            print(f"{enemy['name']}'s defense is too high! Try using spells!")
    if choice == "1":
        print(f"{character['spells']}")
        spell_choice = input("Type the spell's name: ")
        if spell_choice not in character['spells']:
            print("No such spell exists!\nOh no, you've been caught off-guard!")
        elif character["mana"] - character["spells"][spell_choice]["cost"] < 0:
            print("Not enough mana!")
        elif character["spells"][spell_choice]["target"] == "player":
            character["mana"] -= character["spells"][spell_choice]["cost"]
            character["health"] += character["spells"][spell_choice]["strength"]
            print(f"You have {character['health']} HP and {character['mana']} mana.")
        else:
            before = enemy["health"]
            character["mana"] -= character["spells"][spell_choice]["cost"]
            enemy["health"] -= character["spells"][spell_choice]["strength"]
            print(f"You have dealt {before - enemy['health']} damage!\n"
                  f"The enemy has {enemy['health']} HP.")
    if choice == "2":
        enemy["run"] = True


def death_message():
    """
    Display a death message

    :return:
    """
    message = random.randint(1, 3)
    with open("dialogue.txt", encoding='utf-8') as file_object:
        lines = file_object.readlines()
        if message == 1:
            print("".join(lines[23:31]))
        if message == 2:
            print("".join(lines[31:37]))
        if message == 3:
            print("".join(lines[37:45]))
    choice = input("Press ENTER to continue \n or type \"quit\" to quit")
    if choice != "QUIT".lower:
        print("Teleporting to start...")
    else:
        return  # quit game


def engage_battle(character, enemy):
    """
    Display to the player what options they can take in combat.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :precondition: enemy must be a dictionary containing the fields of an enemy dictionary
    :postcondition: character["health"] is increased, decreased, or remains the same
    :postcondition: character["mana"] is decreased or remains the same
    :postcondition: character["win"] becomes True or remains the same
    :postcondition: character["location"] changes or remains the same
    :postcondition: enemy["health"] is decreased or remains the same
    :postcondition: enemy["run"] becomes True or remains the same
    :return: none
    """
    print(f"You have entered combat with {enemy['name']}")
    while character["health"] > 0 and enemy["health"] > 0 and enemy["run"] is False:
        if character["speed"] >= enemy["speed"]:
            battle_options(character, enemy)
            if enemy["health"] > 0 and enemy["run"] is False:
                enemy_turn(character, enemy)
        else:
            enemy_turn(character, enemy)
            if character["health"] > 0:
                battle_options(character, enemy)
    if character["health"] <= 0:
        death_message()  # quit game if player wants
        character["position"] = game.START
        character["health"] = character["max_health"]
    elif enemy["health"] <= 0:
        if enemy["is_boss"]:
            character["win"] = True
        print(f"You have defeated {enemy['name']}.")
        calculate_exp(character, enemy)
    elif enemy["run"] is True:
        print(f"Successfully escaped from {enemy['name']}.")


def calculate_exp(character, enemy):
    """
    Calculate the experience a character is given and if they level up.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: character must be a dictionary containing the fields of a character dictionary
    :precondition: enemy must be a dictionary containing the fields of an enemy dictionary
    :postcondition: character["level"] is increased or remains the same
    :postcondition: character["current_exp"] is increased or remains the same
    :postcondition: character["exp_needed"] is increased or remains the same
    return: none
    """
    if character["exp_needed"] <= enemy["exp_value"]:
        game.level_up(character)
    else:
        character["current_exp"] += enemy["exp_value"]
        print(f"Gained {enemy['exp_value']} EXP.\n")
        character["exp_needed"] = game.exp_to_level_up(character)


def main():
    """
    Runs the program.
    """
    test_character = game.make_character("Beta Tester")
    test_enemy = make_enemy("Beta Tester Killer", 999, 999, 999, 999)
    engage_battle(test_character, test_enemy)


if __name__ == "__main__":
    main()
