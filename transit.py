"""
Elijah Fabon
A01324170
Jihoon Yoon
A01322277
"""

import json
import ast
import game_2


def display_transit(line):
    """

    :param line:
    :return:
    """
    stations = {}
    with open("transit.json") as file_object:
        lines = json.load(file_object)
        for station_number, name in enumerate(lines[line]):
            print(station_number, name)
            stations[station_number] = name
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


def main():


if __name__ == '__main__':
    main()