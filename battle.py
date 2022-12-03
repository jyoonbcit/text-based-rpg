"""
Elijah Fabon
A01324170
"""


def battle_options():
    options = ["Attack", "Skill", "Defend", "Run"]
    print("Make your decision:")
    for decision, option in enumerate(options, 0):
        print(decision, option)
    choice = input()
    if choice != "0" or choice != "1" or choice != "2" or choice != "3":
        print("Invalid choice!")
    elif choice == "0":
        pass
    elif choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass


def engage_battle(character, enemy):
    print(f"You have entered combat with {enemy['name']}")
    battle_options()


def main():
    battle_options()


if __name__ == "__main__":
    main()
