import re
from collections import defaultdict

def process_data():
    with open("data/day_16") as f:
        data = f.read().split("\n\n")

    tickets = data[0]
    my_ticket = data[1].split("\n")[1:][0].split(",")
    nearby_tickets = data[2].split("\n")[1:]
    return tickets, my_ticket, nearby_tickets

tickets, my_ticket, nearby_tickets = process_data()

def get_valid_tickets(tickets):
    location_valid_tickets = defaultdict(set)
    for row in tickets.split("\n"):
        location = row.split(":")[0]
        split = row.split(" or ")
        for part in split:
            nums = re.findall(r"\d+", part)
            nums = [int(num) for num in nums]
            for x in range(min(nums), max(nums) + 1):
                location_valid_tickets[location].add(int(x))
    return location_valid_tickets


def get_ticket_scanning_error_rate(location_valid_tickets, nearby_tickets):
    total = 0
    valid_tickets = []
    for tickets in location_valid_tickets.values():
        for ticket in tickets:
            valid_tickets.append(ticket)

    discared = set()
    for ticket in nearby_tickets:
        for num in ticket.split(","):
            if int(num) not in valid_tickets:
                total += int(num)
                discared.add(ticket)
    valid_tickets = set(nearby_tickets) - set(discared)
    return total, valid_tickets

print("Part 1")
location_valid_tickets = get_valid_tickets(tickets)
error_rate, valid_tickets = get_ticket_scanning_error_rate(
    location_valid_tickets, nearby_tickets
)
print(error_rate)

def determine_order_of_fields(location_valid_tickets, valid_tickets):
    
    valid_tickets = list(valid_tickets)
    columns = len(valid_tickets[0].split(","))
    rows = len(valid_tickets)
    ticket_matrix = [ [ [] for _ in range(columns)] for _ in range(rows) ]
    for row_index, row in enumerate(valid_tickets):
        split = row.split(",")
        for col_index, num in enumerate(split):
            ticket_matrix[row_index][col_index] = int(num)

    col_to_tickets = defaultdict(list)
    for col in range(0, columns):
        for row in range(0, rows):
            col_to_tickets[col].append(ticket_matrix[row][col])
    
    valid_cols = {}
    for location, valid_tickets in location_valid_tickets.items():
        valid_cols[location] = []
        for col, tickets in col_to_tickets.items():
            found = True
            for ticket in tickets:
                if ticket not in valid_tickets:
                    found = False
                    break
            if found:
                valid_cols[location].append(col)

    # Solve col -> field
    solved_cols = []
    col_to_location = {}
    for i in range(0, columns):
        for location, possible_cols in valid_cols.items():
            if len(possible_cols) == i + 1:
                for j in possible_cols:
                    if j not in solved_cols:
                        solved_cols.append(j)
                        col_to_location[location] = j
                        break
    
    return col_to_location

print("Part 2")
order_of_fields = determine_order_of_fields(location_valid_tickets, valid_tickets)
total = 1
for field, col in order_of_fields.items():
    if 'departure' in field:
        total *= int(my_ticket[col])
print(total)