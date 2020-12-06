from functools import reduce

def create_slopes(parsed_map, right, down):
    tree_count = 0
    x, y = 0, 0
    width = len(parsed_map[x])
    while y < len(parsed_map):
        current_line = parsed_map[y]
        if x > len(parsed_map[y]) - 1:
            x = x % width
        if current_line[x] == "#":
            tree_count += 1
        x += right
        y += down
    return tree_count


if __name__ == "__main__":
    with open('./data/day_3', 'r') as f:
        map_data = f.readlines()
        map_data = [line.replace("\n", "") for line in map_data]
    print("Part 1: ", create_slopes(map_data, 3, 1))

    trees_per_slope = []
    positions = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for pos in positions:
        trees_per_slope.append(create_slopes(map_data, pos[0], pos[1]))
    
    multiplied = reduce(lambda x, y: x*y, trees_per_slope)
    print("Part 2: ", multiplied)
