def find_sum_2020(expense_report):
    for report_value in expense_report:
        if (2020-report_value) in expense_report:
            return report_value, 2020-report_value

def find_sum_2020_3_values(expense_report):
    # Brute force :)
    for first_val in expense_report:
        for second_val in expense_report:
            for third_val in expense_report:
                if (2020 - first_val - second_val - third_val) == 0:
                    return first_val, second_val, third_val
        

if __name__ == "__main__":
    with open('./data/day_1', 'r') as f:
        expense_report = f.read().splitlines()

    expense_report = [int(report_value) for report_value in expense_report]
    print("Day 1 - part one")
    entry_one, entry_two = find_sum_2020(expense_report)
    print(entry_one*entry_two)

    print("Day 2 - part two")
    entry_one, entry_two, entry_three = find_sum_2020_3_values(expense_report)
    print(entry_one * entry_two * entry_three)