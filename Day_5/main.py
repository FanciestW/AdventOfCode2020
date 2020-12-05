import os
import re
import math

def read_file(file_name: str) -> list[str]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while(True):
            line = read_file.readline().strip()
            if not line:
                break
            if (re.match('^[FB]{7}[RL]{3}$', line)):
                data.append(line)
        return data
    except Exception as e:
        print(str(e))

def get_seat(pass_str: str, row_count=128, col_count=8) -> int:
    rows = [i for i in range(row_count)]
    cols = [i for i in range(col_count)]
    for c in pass_str[:-3]:
        if c == 'F':
            rows = rows[:math.ceil(len(rows) / 2)]
        elif c == 'B':
            rows = rows[math.ceil(len(rows) / 2):]
    
    for c in pass_str[-3:]:
        if c == 'L':
            cols = cols[:math.ceil(len(cols) / 2)]
        elif c == 'R':
            cols = cols[math.ceil(len(cols) / 2):]
    
    return rows[0] * 8 + cols[0]

def find_seat_id(seat_id_list: list[str]) -> int:
    for i in range(min(seat_id_list), max(seat_id_list)):
        if i not in seat_id_list:
            return i
    return -1

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(max([get_seat(d) for d in data]))
    # > 878

    seat_ids = [get_seat(d) for d in data]
    print(find_seat_id(seat_ids))