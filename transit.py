"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""

import json
import ast
import game_2


def you_want_a_ride():
    choices = ["Yes", "No"]
    decisions = {choice: name for choice, name in enumerate(choices, 1)}
    print("Do you want a ride?")
    for choice, name in enumerate(choices, 1):
        print(choice, name)
    decision = int(input("ENTER number:"))
    while decision not in decisions.keys():
        print("Invalid input. Try again")
        decision = int(input("Do you want a ride?"))
    choice = decisions[decision]
    if choice == "Yes":
        return True
    else:
        return False


def which_line(character):
    all_lines = {"Expo line": [(1, 5), (1, 4), (2, 5), (3, 6), (6, 8)],
                 "Canada line": [(1, 5), (1, 4), (3, 4), (6, 4), (8, 4), (9, 3)],
                 "R4 Bus Route": [(3, 0), (6, 4), (6, 8)],
                 "99B line": [(3, 0), (3, 4)],
                 "Seabus": [(1, 5), (0, 7)]}
    lines_available = list(filter(lambda element: character["position"] in element[1], all_lines.items()))
    decisions = {choice: name[0] for choice, name in enumerate(lines_available, 1)}
    location = character["position"]
    print(f"Which line do you want to take? You are at {location}")
    for choice, name in enumerate(lines_available, 1):
        print(choice, name[0])
    decision = int(input("ENTER number:"))
    while decision not in decisions.keys():
        print("That is not in the the transit system. Try again.")
        decision = int(input("ENTER number:"))
    return decisions[decision]


def display_transit(line):
    """

    :param line:
    :return:
    """
    with open("transit.json") as file_object:
        lines = json.load(file_object)
        stations = {station_number: name for station_number, name in enumerate(lines[line], 1)}
        for station_number, name in enumerate(lines[line], 1):
            print(station_number, name)
    return stations


def transport(stations, line, character):
    """

    :param stations:
    :param line:
    :param character:
    :return:
    """
    destination = int(input("ENTER number:"))
    while destination not in stations.keys():
        print("That is not a station. Try again.")
        destination = int(input("Where do you want to go?"))
    with open("transit.json") as transit:
        station = json.load(transit)
        transit_line = station[line]
        character["position"] = ast.literal_eval(transit_line[stations[destination]])


def ride_transit(character):
    """

    :param character:
    """
    line = which_line(character)
    location = character["position"]
    print(f"Which line do you want to take? You are at {location}")
    if line == "Expo line":
        transport(display_transit("Expo_line"), "Expo_line", character)
    elif line == "Canada line":
        transport(display_transit("Canada_line"), "Canada_line", character)
    elif line == "R4 Bus Route":
        transport(display_transit("R4_bus_route"), "R4_bus_route", character)
    elif line == "99B line":
        transport(display_transit("99B_line"), "99B_line", character)
    else:
        transport(display_transit("Seabus"), "Seabus", character)


def transit_available(character):
    transit = [(0, 7), (1, 5), (1, 4), (2, 5), (3, 0), (3, 4), (3, 6), (6, 4), (6, 8), (8, 4), (9, 3)]
    if character["position"] in transit:
        print("Transit is available")
        return True
    else:
        return False


def main():
    test_character = game_2.make_character("Beta Tester")
    test_character["position"] = (1, 5)
    print(test_character["position"])
    if transit_available(test_character):
        if you_want_a_ride():
            ride_transit(test_character)
        else:
            print("You don't want a ride")
    print(test_character["position"])


if __name__ == '__main__':
    main()
