from collections import Counter

def count_answers(answers):
    count = 0
    total_unique = set()
    for answer in answers:
        for person in answer:
            unique = (set(list(Counter(person).keys())))
            total_unique.update(unique)
        count += len(total_unique)
        total_unique = set()
    return count


def count_all_answered(answers):
    count = 0
    for grouped_answer in answers:
        answered_yes = []
        letter_seen = set()
        for person_answers in grouped_answer:
            for letter in person_answers:
                if letter not in letter_seen and is_contained_in_all_lists(letter, grouped_answer):
                    answered_yes.append(letter)
                letter_seen.add(letter)
        count += len(answered_yes)
    return count


def is_contained_in_all_lists(letter, group_answers):
    for person_answers in group_answers:
        if letter not in person_answers:
            return False
    return True


if __name__ == "__main__":
    with open('data/day_6', 'r') as f:
        data = f.read().split("\n\n")
        answers = [[person for person in line.split("\n")] for line in data]

    print(count_answers(answers))
    print(count_all_answered(answers))
