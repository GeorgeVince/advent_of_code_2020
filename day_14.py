from collections import defaultdict
from itertools import combinations_with_replacement  
import copy

def process_data():
    with open('data/day_14') as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
    return data

docking_data = process_data()

# Part 1
def process_docking_data(docking_data):
    total = 0
    addresses = defaultdict(lambda: bin(10))
    for line in docking_data:
        if 'mask' in line:
            mask = line.split("=")[1].strip()
        else:
            split = line.split("=")
            to_add = int(split[1])
            mem_addr = int(split[0].replace("mem[", "").replace("]",""))
            addresses[mem_addr] = add_to_mem_address(to_add, mask)
    total += sum(addresses.values())
    return(total)

# Part 2
def process_docking_data_v2(docking_data):
    total = 0
    addresses = defaultdict(lambda: bin(10))
    for line in docking_data:
        if 'mask' in line:
            mask = line.split("=")[1].strip()
        else:
            split = line.split("=")
            to_add = int(split[1])
            mem_addr = int(split[0].replace("mem[", "").replace("]",""))
            mem_addr_bin = list('{:036b}'.format(mem_addr))
            #Apply Mask
            for index, mask_val in enumerate(mask):
                if mask_val != "0":
                    mem_addr_bin[index] = mask_val
            # Generate possibilities
            for address in gen_mem_addr(mem_addr_bin):
                addresses[address] = to_add

    total += sum(addresses.values())
    return(total)



def add_to_mem_address(to_add, mask):
    index_val = {index:val for index, val in enumerate(mask) if val in "10" }
    as_string = list('{:036b}'.format(to_add))
    for index, val in index_val.items():
        as_string[index] = val    
    return(int("".join(as_string), 2))

def gen_mem_addr(addr):
    
    if 'X' not in addr:
        return ["".join(addr)]
    
    addresses = []
    x_pos = addr.index('X')
    
    tmp_0 = addr.copy()
    tmp_1 = addr.copy()
    tmp_0[x_pos] = "0"
    tmp_1[x_pos] = "1"
    
    addresses.extend(gen_mem_addr(tmp_0))
    addresses.extend(gen_mem_addr(tmp_1))

    return addresses

# print("Part 1:")
# print(process_docking_data(docking_data))

print("Part 2:")
print(process_docking_data_v2(docking_data))
