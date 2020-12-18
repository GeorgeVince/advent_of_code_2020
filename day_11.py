from pprint import pprint
from copy import deepcopy
from itertools import product


def process_data():
    with open('data/day_11') as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        data = [[char for char in line] for line in data]
    return data


SEAT_LAYOUT = process_data()
COLUMNS = len(SEAT_LAYOUT[0]) - 1
ROWS = len(SEAT_LAYOUT) - 1
EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

# E.g. N (-1, 0), E (0, 1)
possible_directions = product(list(range(-1, 2)), list(range(-1, 2)))
directions = [x for x in possible_directions if x != (0, 0)]


def check_surrounding(seat_layout, row, col, first_only=False):
    surrounding_seats = []
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if not first_only:
            if new_row <= ROWS and new_row >= 0 and new_col <= COLUMNS and new_col >= 0:
                surrounding_seats.append(seat_layout[new_row][new_col])
        elif first_only:
            while new_row <= ROWS and new_row >= 0 and new_col <= COLUMNS and new_col >= 0:
                if seat_layout[new_row][new_col] in [EMPTY, OCCUPIED]:
                    surrounding_seats.append(seat_layout[new_row][new_col])
                    break
                new_row = new_row + direction[0]
                new_col = new_col + direction[1]

    return surrounding_seats


def simulate_swaps(seat_layout, first_only, occupied_count):
    new_layout = deepcopy(seat_layout)
    has_changes = True
    while has_changes:
        has_changes = False
        old_layout = deepcopy(new_layout)
        for row in range(0, ROWS + 1):
            for col in range(0, COLUMNS + 1):
                if old_layout[row][col] == FLOOR:
                    continue
                surrounding_seats = check_surrounding(
                    old_layout, row, col, first_only)
                if old_layout[row][col] == EMPTY and \
                    surrounding_seats.count(OCCUPIED) == 0:
                    new_layout[row][col] = OCCUPIED
                    has_changes = True
                elif old_layout[row][col] == OCCUPIED and \
                     surrounding_seats.count(OCCUPIED) >= occupied_count:
                    new_layout[row][col] = EMPTY
                    has_changes = True
    
    total_occupied_seats = sum(
        sum([seat == OCCUPIED for seat in line]) for line in new_layout)
    return total_occupied_seats


print("Part 1")
print(simulate_swaps(SEAT_LAYOUT, first_only=False, occupied_count=4))

print("Part 2")
print(simulate_swaps(SEAT_LAYOUT, first_only=True, occupied_count=5))
