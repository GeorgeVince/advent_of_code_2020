def process_data():
    with  open('data/day_8') as f:
        data = f.readlines()
        data = [line.replace("\n", "").split(" ") for line in data]
    return data

def acc_value_and_fully_processed(instructions):
    not_seen = True
    fully_processed = False
    seen = set()
    acc = 0
    curr_indx = 0    
    while not_seen:
        if curr_indx not in seen:
            seen.add(curr_indx)
        else:
            break

        curr_instruction = instructions[curr_indx] 
        instruction, val = curr_instruction[0], curr_instruction[1]
        
        if instruction == "nop":
            curr_indx +=1
        
        if instruction == "jmp":
            curr_indx += int(val)
        
        if instruction == "acc":
            acc += int(val)
            curr_indx += 1

        if curr_indx == len(instructions):
            fully_processed = True
            break

    return acc, fully_processed

instructions = process_data()

print("Part 1")
print(acc_value_and_fully_processed(instructions))

swap = {'jmp':'nop', 'nop':'jmp'}
print("Part 2")
for instruction in instructions:
    if instruction[0] == 'jmp' or instruction[0] == 'nop':
        instruction[0] = swap[instruction[0]]
        acc, fully_processed = acc_value_and_fully_processed(instructions)
        if fully_processed:
            print(acc)
        instruction[0] = swap[instruction[0]]
