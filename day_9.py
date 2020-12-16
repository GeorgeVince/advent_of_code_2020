from itertools import combinations_with_replacement    

def process_data():
    with  open('data/day_9') as f:
        data = f.readlines()
        data = [int(line.replace("\n", "")) for line in data]
    return data

xmas_input = process_data()

def find_first_invalid_number(xmas_input):
    preamble = 25
    for indx, num in enumerate(xmas_input[preamble:]):
        combs = combinations_with_replacement  (xmas_input[indx:indx+preamble], 2)
        is_valid = (any(sum(combination) == num for combination in combs))
        if not is_valid:
            return(num)
        
def find_contiguous_set(xmas_input):
    # Brute force :) 
    invalid_number = find_first_invalid_number(xmas_input)
    for i in range(0, len(xmas_input)-1):
        for j in range(1, len(xmas_input)-1):
            stack = xmas_input[i:j]
            if sum(stack) == invalid_number:
                return min(stack) + max(stack)

print("Part 1")
print(find_first_invalid_number(xmas_input))

print("Part 2")
print(find_contiguous_set(xmas_input))