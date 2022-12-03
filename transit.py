"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""

import json
import ast
import game_2


def do_you_want_a_ride():
    choices = ["Yes", "No"]
    decisions = {choice: name for choice, name in enumerate(choices, 1)}
    for choice, name in enumerate(choices, 1):
        print(choice, name)
    decision = input("Do you want a ride?")
    while decision not in decisions:
        print("Invalid input. Try again")
        decision = input("Do you want a ride?")
    return decisions[decision]


def which_line(character):
    all_lines = {"Expo line": [(1, 5), (1, 4), (2, 5), (3, 6), (6, 8)],
                 "Canada line": [(1, 5), (1, 4), (3, 4), (6, 4), (8, 4), (9, 3)],
                 "R4 Bus Route": [(3, 0), (6, 4), (6, 8)],
                 "99B line": [(3, 0), (3, 4)],
                 "Seabus": [(1, 5), (0, 7)]}
    lines_available = list(filter(lambda element: character["position"] in element[1], all_lines.items()))
    decisions = {choice: name for choice, name in enumerate(lines_available, 1)}
    for choice, name in enumerate(lines_available, 1):
        print(choice, name)
    decision = input("Which line do you want to take?")
    while decision not in decisions:
        print("That is not in the the transit system. Try again.")
        decision = input("Which line do you want to take?")
    return decisions[decision]


def display_transit(line):
    """

    :param line:
    :return:
    """
    with open("transit.json") as file_object:
        lines = json.load(file_object)
        stations = {station_number: name for station_number, name in enumerate(lines[line])}
        for station_number, name in enumerate(lines[line]):
            print(station_number, name)
    return stations


def transport(stations, line, character):
    """

    :param stations:
    :param line:
    :param character:
    :return:
    """
    destination = input("Where do you want to go?")
    while destination not in stations:
        print("That is not a station. Try again.")
        destination = input("Where do you want to go?")
    with open("transit.json") as transit:
        station = json.load(transit)
        character["position"] = ast.literal_eval(station[line[destination]])


def ride_transit(line, character):
    """

    :param line:
    :param character:
    :return:
    """
    if line in ("Waterfront (Expo line)", "Granville Station", "Science World/Chinatown Station",
                "Commercial/Broadway Station", "Joyce Collingwood Station (Expo line)"):
        transport(display_transit("Expo_line"), "Expo_line", character)
    elif line in ("Waterfront (Canada Line)", "Vancouver City Centre Station",
                  "Broadway City Hall Station (Canada line)", "Oakridge 41st Station (Canada line)",
                  "Marine Drive Station", "YVR Airport Station"):
        transport(display_transit("Canada_line"), "Canada_line", character)
    elif line in ("UBC Exchange Station (R4)", "Oakridge 41st Station (R4)", "Joyce Collingwood Station (R4)"):
        transport(display_transit("R4_bus_route"), "R4_bus_route", character)
    elif line in ("UBC Exchange Station (99B Line)", "Broadway City Hall Station"):
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
    print(test_character["position"])


if __name__ == '__main__':
    main()
