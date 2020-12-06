
MAX_ROWS = 127
MAX_COLUMNS = 7
MIN_ROWS = 0
MIN_COLUMNS = 0


def get_row_from_id(row_ids):
    min_, max_ = MIN_ROWS, MAX_ROWS

    for index, char in enumerate(row_ids):
        if char == 'F':
            min_, max_ = take_lower(min_, max_)
        else:
            min_, max_ = take_upper(min_, max_)
        if index == len(row_ids)-1:
            if char == 'F':
                return min_
            else:
                return max_


def get_column_from_id(col_ids):
    min_, max_ = MIN_COLUMNS, MAX_COLUMNS
    for index, char in enumerate(col_ids):
        if char == 'L':
            min_, max_ = take_lower(min_, max_)
        else:
            min_, max_ = take_upper(min_, max_)
        if index == len(col_ids)-1:
            if char == 'L':
                return min_
            else:
                return max_


def take_lower(min_, max_):
    max_ = (max_ - min_) // 2 + min_
    return min_, max_


def take_upper(min_, max_):
    min_ = (max_ - min_) // 2 + min_ + 1
    return min_, max_


if __name__ == "__main__":
    with open('./data/day_5', 'r') as f:
        data = f.readlines()
    seat_ids = [line.replace("\n", "") for line in data]

    boarding_ids = []
    for seat_id in seat_ids:
        row_ids = seat_id[0:7]
        col_ids = seat_id[7:]
        row = get_row_from_id(row_ids)
        column = get_column_from_id(col_ids)
        seat_id = row * 8 + column
        boarding_ids.append(seat_id)
    

    print("Max ID: ", max(boarding_ids))
    missing_seats = []
    for boarding_id in range(0, max(boarding_ids)):
        if boarding_id not in boarding_ids:
            if boarding_id-1 in boarding_ids and boarding_id+1 in boarding_ids:
                missing_seats.append(boarding_id)
    print(missing_seats)
