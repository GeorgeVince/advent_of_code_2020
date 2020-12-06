
from collections import Counter


def is_valid_password_v1(accepted_range, char, password):
    min_occurances, max_occurances = accepted_range.split("-")
    occurances = Counter(password)[char]
    return int(min_occurances) <= occurances <= int(max_occurances)


def day_two_part_one():
    with open("./data/day_2", 'r') as f:
        data = f.readlines()

    count = 0
    for line in data:
        accepted_range, char, password = line.replace(
            '\n', "").replace(":", "").split(" ")
        if is_valid_password_v1(accepted_range, char, password):
            count += 1
    print(count)


def is_valid_password_v2(accepted_positions, char, password):
    pos_one, pos_two = accepted_positions.split("-")
    pos_one = int(pos_one)
    pos_two = int(pos_two)
    pos_one_char, pos_two_char = None, None

    pos_one_char = password[pos_one-1]
    pos_two_char = password[pos_two-1]

    return (pos_one_char == char) ^ (pos_two_char == char)


def day_two_part_two():
    with open("./data/day_2", 'r') as f:
        data = f.readlines()

    count = 0
    for line in data:
        accepted_positions, char, password = line.replace(
            '\n', "").replace(":", "").split(" ")
        if is_valid_password_v2(accepted_positions, char, password):
            count += 1
    print(count)


if __name__ == "__main__":
    day_two_part_two()
    is_valid_password_v2("3-5", "v", "qvjjdhvl")
    is_valid_password_v2("1-3", "b", "cdefg")


