def process_data():
    with open('data/day_12') as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
    return data


COORDS = {"N": (-1, 0), "E": (0, 1), "S":(1, 0), "W":(0, -1)}
DIRECTIONS = ["N", "E", "S", "W"]

instructions = process_data()

def new_direction(current_direction, direction, amount):
    amount = amount / 90 
    cur_index = DIRECTIONS.index(current_direction)
    if direction == "R":
        new_index = (cur_index + amount) % len(DIRECTIONS)
    elif direction == "L":
        new_index = (cur_index - amount) % len(DIRECTIONS)
    return DIRECTIONS[int(new_index)]

def move_coordinates(coords, direction, amount):
    offset = COORDS[direction]
    coords[0] += amount * offset[0]
    coords[1] += amount * offset[1]
    return coords

def process_instructions(instructions):
    current_direction = "E"
    coords = [0, 0]
    for instruction in instructions:
        direction, amount = instruction[0], int(instruction[1:])
        if direction in ["L", "R"]:
            current_direction = new_direction(current_direction, direction, amount)
        elif direction in "F":
            coords = move_coordinates(coords, current_direction, amount)
        else:
            coords = move_coordinates(coords, direction, amount)
    return coords

print("Part 1")
new_coords = process_instructions(instructions)
print(abs(new_coords[0]) + abs(new_coords[1]))