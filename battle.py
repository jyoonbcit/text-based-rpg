"""
Elijah Fabon
A01324170
"""


def make_enemy(name, exp_value):
    enemy = {"name": name,
             "health": 100,
             "attack": 1,
             "defense": 1,
             "speed": 2,
             "exp_value": exp_value}
    return enemy


def encounter_enemy():
    pass


def battle_options(character, enemy):
    options = ["Attack", "Skill", "Defend", "Run"]
    print("Make your decision:")
    for decision, option in enumerate(options, 0):
        print(decision, option)
    choice = input()
    if choice != "0" or choice != "1" or choice != "2" or choice != "3":
        print("Invalid choice!")
    elif choice == "0":
        enemy["health"] -= character["attack"]
    elif choice == "1":
        print(f"{character['spells']}")
        spell_choice = input("Type the spell's name: ")
        if character["spells"][spell_choice][0] == "player":
            character["health"] += character["spells"][spell_choice][1]
            print(f"You have {character['health']} HP remaining.")
        else:
            enemy["health"] -= character["spells"][spell_choice][1]
    elif choice == "2":
        if enemy["attack"] - character["defense"] < 0:
            pass
        else:
            character["health"] -= enemy["attack"] - character["defense"]
            print(f"You have taken {enemy['attack'] - character['defense']} damage!")
            print(f"You now have {character['health']} HP.")
    elif choice == "3":
        return


def engage_battle(character, enemy):
    print(f"You have entered combat with {enemy['name']}")
    while character["health"] > 0 and enemy["health"] > 0:
        battle_options()


def main():
    battle_options()


if __name__ == "__main__":
    main()
