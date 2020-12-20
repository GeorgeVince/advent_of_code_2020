import math
# Because cba implementing crt
from sympy.ntheory.modular import crt 


def process_data():
    with open('data/day_13') as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
    return data


bus_notes = process_data()
desired_time = int(bus_notes[0])
depart_ids = [int(time) for time in bus_notes[1].split(",") if time != "x"]


def find_closest_time(desired_time, depart_ids):
    id_time = {}
    for depart_id in depart_ids:
        distance = ((math.ceil(desired_time/depart_id))
                    * depart_id) - desired_time
        id_time[depart_id] = distance

    min_key = min(id_time, key=id_time.get)
    return min_key * id_time[min_key]


depart_ids_with_unknowns = [time for time in bus_notes[1].split(",")]

def find_consecutive_offsets(depart_ids_with_unknowns):
    id_position = {int(bus_id): depart_ids_with_unknowns.index(bus_id)
                   for bus_id in depart_ids_with_unknowns if bus_id != "x"}
    mods = list(id_position.keys())
    offsets = [-offset for offset in id_position.values()]
    lowest_multiple, _ = crt(mods, offsets)
    return lowest_multiple


print("Part 1")
print(find_closest_time(desired_time, depart_ids))

print("Part 2")
print(find_consecutive_offsets(depart_ids_with_unknowns))
