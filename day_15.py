data = [0, 3, 1, 6, 7, 5]

def memory_game(size):
    seen = {}

    for i in range(len(data) - 1):
        num = data[i]
        seen[num] = i

    for i in range(len(data) - 1, size - 1):
        num = data[i]

        if num not in seen:
            data.append(0)
            seen[num] = i

        else:
            last_seen = seen[num]
            newNum = i - last_seen
            data.append(newNum)
            seen[num] = i

    return data[-1]


print("Part 1")
print(memory_game(2020))
print("Part 2")
print(memory_game(30000000))
