import re


def lines_to_passport(lines):
    passports = []
    passport = ""
    for line in lines:
        passport += line + " "
        if line.strip() == "":
            passports.append(parse_passport(passport.rstrip()))
            passport = ""
    return passports


def has_all_required_keys(passport):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    optional = {'cid'}
    return required_keys.issubset(set(passport.keys()))


def passes_validation(passport):
    field_validation = {'byr': passes_min_max(passport['byr'], 1920, 2002),
                        'iyr': passes_min_max(passport['iyr'], 2010, 2020),
                        'eyr': passes_min_max(passport['eyr'], 2020, 2030),
                        'hgt': is_valid_height(passport['hgt']),
                        'hcl': is_valid_hair_colour(passport['hcl']),
                        'ecl': is_valid_eye_colour(passport['ecl']),
                        'pid': is_valid_passport_id(passport['pid'])}

    return all(field_validation.values())

def is_valid_passport_id(pid):
    regex = "([0-9]){9}"
    found = re.search(regex, pid)
    return True if found and len(pid) == 9 else False


def is_valid_eye_colour(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_hair_colour(hcl):
    regex = "#([0-9a-f]){6}"
    found = re.search(regex, hcl)
    return True if found and len(hcl) == 7 else False


def is_valid_height(hgt):
    if 'cm' in hgt and 'in' in hgt:
        return False

    if 'cm' in hgt:
        split_by = 'cm'
        min_hgt = 150
        max_hgt = 193
    elif 'in' in hgt:
        split_by = 'in'
        min_hgt = 59
        max_hgt = 76
    else:
        return False

    hgt = hgt.split(split_by)[0]
    return hgt.isdigit() and (passes_min_max(hgt, min_hgt, max_hgt))


def passes_min_max(val, min, max):
    return min <= int(val) <= max


def parse_passport(passport_line):
    """hgt:159cm pid:5610 -> dict{k:v}"""
    parts = passport_line.split(" ")
    return {x[0]: x[1] for x in [part.split(":") for part in parts]}


if __name__ == "__main__":
    with open('./data/day_4', 'r', newline="") as f:
        data = f.readlines()

    lines = [line.replace("\r\n", "") for line in data]

    passports = lines_to_passport(lines)

    print("Part one:")
    print(sum(1 for passport in passports if has_all_required_keys(passport)))

    print("Part two:")
    print(sum(1 for passport in passports if has_all_required_keys(
        passport) and passes_validation(passport)))
