"""
Elijah Fabon
A01324170
"""
import game


def make_enemy(name, health, attack, defense, exp_value, speed=1):
    enemy = {"name": name,
             "health": health,
             "attack": attack,
             "defense": defense,
             "speed": speed,
             "exp_value": exp_value,
             "run": False}
    return enemy


def encounter_enemy():
    pass


def enemy_turn(character, enemy):
    if character["defense"] > enemy["attack"]:
        print(f"You have taken 0 damage from {enemy['name']}.")
    else:
        character["health"] -= enemy["attack"]
        print(f"You have taken {enemy['attack'] - character['defense']} damage from {enemy['name']}.\n"
              f"You have {character['health']} HP and {character['mana']} mana.")


def battle_options(character, enemy):
    options = ["Attack", "Skill", "Run"]
    print("Make your decision:")
    for decision, option in enumerate(options, 0):
        print(decision, option)
    choice = input()
    if choice != "0" and choice != "1" and choice != "2":
        print(f"{character['name']} does not understand your command!\nOh no, you've been caught off-guard!")
    elif choice == "0":
        enemy["health"] -= character["attack"]
    elif choice == "1":
        print(f"{character['spells']}")
        spell_choice = input("Type the spell's name: ")
        if character["mana"] - character["spells"][spell_choice]["cost"] < 0:
            print("Not enough mana!")
        elif character["spells"][spell_choice]["target"] == "player":
            character["health"] += character["spells"][spell_choice]["strength"]
            print(f"You have {character['health']} HP and {character['mana']} mana.")
        else:
            before = enemy["health"]
            enemy["health"] -= character["spells"][spell_choice]["strength"]
            print(f"You have dealt {before - enemy['health']} damage!\n"
                  f"The enemy has {enemy['health']} HP.")
    else:
        enemy["health"] = "run"


def engage_battle(character, enemy):
    print(f"You have entered combat with {enemy['name']}")
    while character["health"] > 0 and enemy["health"] > 0 and enemy["run"] is False:
        battle_options(character, enemy)
        enemy_turn(character, enemy)
    if character["health"] <= 0:
        print("You have died. Teleporting to hospital...")
        # implement teleport to hospital
    elif enemy["health"] < 0:
        print(f"You have defeated {enemy['name']}.")
        calculate_exp(character, enemy)
    elif enemy["run"] is True:
        print(f"Successfully escaped from {enemy['name']}.")


def calculate_exp(character, enemy):
    if character["exp_needed"] < enemy["exp_value"]:
        character["current_exp"] += enemy["exp_value"]
        character["exp_needed"] -= enemy["exp_value"]
    else:
        game.level_up(character)


def main():
    test_character = game.make_character("Beta Tester")
    test_enemy = make_enemy("Beta Tester Killer", 999, 999, 999, 999)
    engage_battle(test_character, test_enemy)


if __name__ == "__main__":
    main()
