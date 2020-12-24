import re

def parse_data():
    with open("./data/day_19") as f:
        data = f.read().splitlines()
        rules = [line for line in data if ":" in line]
        letters = [line for line in data if ":" not in line and line != ""]
    return letters, rules

def compute(rules, letters):
    rules_exp = {}
    for rule in rules:
        rule = rule.replace('"', "")
        k, v = rule.split(": ")[0], rule.split(": ")[1]
        rules_exp[k] = v

    def _get_expression(s):
        if s == "|":
            return s
        
        rule_exp = rules_exp[s]
        if rule_exp.isalpha():
            return rule_exp
        else:
            return f'({"".join(_get_expression(part) for part in rule_exp.split())})'
            
    expression_match = re.compile(_get_expression('0'))

    total = 0
    for line in letters:
        if expression_match.fullmatch(line):
            total += 1

    return total

letters, rules = parse_data()

print("Part 1")
print(compute(rules, letters))