def process_data():
    with  open('data/day_10') as f:
        data = f.readlines()
        data = [int(line.replace("\n", "")) for line in data]
    return data

def joltage_differences(joltage_ratings):
    diff_one, diff_three = 0, 0
    for index, rating in enumerate(joltage_ratings):
        if index == 0:
            continue
        difference = joltage_ratings[rating - joltage_ratings[index-1]]
        if difference == 1:
            diff_one +=1
        elif difference == 3:
            diff_three +=1
    return diff_three * diff_one

def get_different_ways(joltage_ratings):
    checked = {}
    def helper(pos):
        # Base Case
        if pos == len(joltage_ratings) - 1:
            return 1
        
        #Memoization
        if pos in checked:
            return checked[pos]

        total = 0
        for i in range(pos + 1, len(joltage_ratings)):
            if joltage_ratings[i] - joltage_ratings[pos] <= 3:
                total += helper(i)
        checked[pos] = total
        return total
    
    return helper(0)
                


joltage_ratings = process_data()
joltage_ratings.extend([0, max(joltage_ratings) +3])
joltage_ratings = sorted(joltage_ratings)

print("Part 1")
print(joltage_differences(joltage_ratings))

print("Part 2")
print(get_different_ways(joltage_ratings))