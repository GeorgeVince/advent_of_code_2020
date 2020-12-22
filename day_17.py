from collections import defaultdict

def parse_x_y_z():
    with open("data/day_17") as f:
        data = f.read().splitlines()
    
    active = []
    for yi, y in enumerate(data):
        for xi, x in enumerate(y):
            if x == "#":
                active.append((yi, xi, 0))
    return active


def simulate_x_y_z(cycles, active):
    for _ in range(0, cycles):
        marked = defaultdict(lambda: 0)
        for x, y, z in active:
            for xi in (-1, 0, 1):
                for yi in (-1, 0, 1):
                    for zi in (-1, 0, 1):
                        if xi == yi == zi == 0:
                            continue
                        new_coord = (x + xi, y + yi, z + zi)
                        marked[new_coord] += 1
        
        new_active = set()
        # Deal with newly active
        for k, v in marked.items():
            if v == 3:
                new_active.add(k)
        # Deal with still active
        for k in active:
            if marked[k] in [2, 3]:
                new_active.add(k)
        active = new_active

    return len(active)

print("Part 1")
starting_input = parse_x_y_z()
print(simulate_x_y_z(6, starting_input))

def parse_x_y_z_w():
    with open("data/day_17") as f:
        data = f.read().splitlines()
    
    active = []
    for yi, y in enumerate(data):
        for xi, x in enumerate(y):
            if x == "#":
                active.append((yi, xi, 0, 0))
    return active

def simulate_x_y_z_w(cycles, active):
    for _ in range(0, cycles):
        marked = defaultdict(lambda: 0)
        for x, y, z, w in active:
            for xi in (-1, 0, 1):
                for yi in (-1, 0, 1):
                    for zi in (-1, 0, 1):
                        for wi in (-1, 0, 1):
                            if xi == yi == zi == wi == 0:
                                continue
                            new_coord = (x + xi, y + yi, z + zi, w + wi)
                            marked[new_coord] += 1
        
        new_active = set()
        # Deal with newly active
        for k, v in marked.items():
            if v == 3:
                new_active.add(k)
        # Deal with still active
        for k in active:
            if marked[k] in [2, 3]:
                new_active.add(k)
        active = new_active
    return (len(active))

print("Part 2")
starting_input = parse_x_y_z_w()
print(simulate_x_y_z_w(6, starting_input))