import re

# Modified from https://stackoverflow.com/questions/2403122/regular-expression-to-extract-text-between-square-brackets
BRACKETS_RE = "(\((?:\[??[^\(]*?\)))"
ADDITION_RE = "\d+\s\+\s\d+"

def process_data():
    with open('data/day_18') as f:
        data = f.read().splitlines()
    return data

def solve_equation(equation):
    equation = equation.replace(")", "").replace("(", "")
    split = equation.split()
    total = int(split[0])
    operation = None
    for char in split[1:]:
        if char.isdigit():
            if operation == "*":
                total *= int(char)
            elif operation == "+":
                total += int(char)
            else:
                AssertionError(f"Unreachable - {char}")
        else:
            operation = char
    return str(total)
    
# Expands all brackets in equation
def expand(equation):
    matched = re.search(BRACKETS_RE, equation)
    while matched is not None:
        solved = solve_equation(matched[0])
        equation = re.sub(BRACKETS_RE, solved, equation, 1)
        matched = re.search(BRACKETS_RE, equation)
    return equation

def expand_solve_additon_first(equation):
    matched = re.search(BRACKETS_RE, equation)
    while matched is not None:
        tmp = matched[0]
        # Within each bracket solve additions
        addition_match = re.search(ADDITION_RE, tmp)
        while addition_match is not None:
            solved = solve_equation(addition_match[0])
            tmp = re.sub(ADDITION_RE, solved, tmp, 1)
            addition_match = re.search(ADDITION_RE, tmp)
        
        
        solved = solve_equation(tmp)
        equation = re.sub(BRACKETS_RE, solved, equation, 1)
        matched = re.search(BRACKETS_RE, equation)

    addition_match = re.search(ADDITION_RE, equation)
    while addition_match is not None:
        solved = solve_equation(addition_match[0])
        equation = re.sub(ADDITION_RE, solved, equation, 1)
        addition_match = re.search(ADDITION_RE, equation)

    return equation

def get_sum_new_operation_order(lines):
    total = 0
    for line in lines:
        expanded = expand(line)
        total += int(solve_equation(expanded))
    return total

def solve_equation_different_precedence(equation):
    # Solve additions first
    equation = expand_solve_additon_first(equation)
    total = solve_equation(equation)
    return total

def get_sum_new_operation_new_precedence(lines):
    total = 0
    for index, line in enumerate(lines):
        total += int(solve_equation_different_precedence(line))

    return total

lines = process_data()
print("Part 1")
print(get_sum_new_operation_order(lines))

print("Part 2")
print(get_sum_new_operation_new_precedence(lines))