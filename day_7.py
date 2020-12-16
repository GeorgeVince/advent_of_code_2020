from collections import defaultdict

def process_data():
    with  open('data/day_7') as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
    return data

bags = process_data()

def construct_bag_graph(bags):
    """
    Returns a graph of 
    Bag : [child:amt, child:amt]
    """
    bag_graph = defaultdict(dict)
    for line in bags:
        split = line.split("contain")
        bag_colour = split[0].replace(" bags", "").rstrip()
        bags_contained = split[1].split(",")
        
        if "contain no other bags" in line:
            bag_graph[bag_colour] = []
            continue

        for bag in bags_contained:
            bag_split = bag.split()
            colour = " ".join([bag_split[1], bag_split[2]])
            amt = bag_split[0]
            bag_graph[bag_colour].update({colour:amt})
    return dict(bag_graph)

def can_contain_shiny_gold(bags_contains):
    cnt = 0
    for bag, children in bags_contains.items():
        to_visit = list(children) # copy!
        if "shiny gold" in to_visit:
            cnt+= 1
            continue
        while len(to_visit) != 0:
            child = to_visit.pop()
            new_children = bags_contains[child]
            if "shiny gold" in new_children:
                cnt += 1
                break
            to_visit.extend(new_children)
    return cnt


def count_bags_inside(inside_bags, bags_contains):
    if inside_bags == {}:
        return 0
    total = 0
    for inner_bag in inside_bags:
        total += ((count_bags_inside(bags_contains[inner_bag], bags_contains) + 1) * int(inside_bags[inner_bag]))
    return total

bags_contains = construct_bag_graph(bags)

# Part 1
print("Part 1")
print(can_contain_shiny_gold(bags_contains))

# Part 2
print("Part 2:")
print(count_bags_inside(bags_contains['shiny gold'], bags_contains))