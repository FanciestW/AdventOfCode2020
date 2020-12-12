import os
from typing import List
import itertools
import copy

def read_file(file_name: str) -> List[List[str]]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline().strip()
            if not line:
                break
            data.append(list(line))
        return data
    except Exception as e:
        print(str(e))
        return []

def pretty_print(data: list):
    for row in data:
        if type(row[0]) is str:
            print(''.join(row))
        else:
            print(row)

def part_1(data: List[List[str]]) -> int:
    seating = data
    did_change = True
    round = 0
    while did_change:
        seating, did_change = seat_move(seating)
        round += 1
    return [c for row in seating for c in row].count('#')
    
def seat_move(data: List[List[str]]) -> List[List[str]]:
    new_seat_map = copy.deepcopy(data)
    did_not_change = True
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c not in ['L', '#']:
                new_seat_map[i][j] = '.'
                continue
            row_i = [i + n for n in range (-1, 2) if i + n >= 0 and i + n < len(data)]
            col_i = [j + n for n in range (-1, 2) if j + n >= 0 and j + n < len(row)]
            coord = [(x, y) for x, y in list(itertools.product(row_i, col_i)) if not (x == i and y == j)]
            neighbors_count = [data[x][y] for x, y in coord].count('#')
            if neighbors_count >= 4:
                new_seat_map[i][j] = 'L'
            elif neighbors_count == 0 and c == 'L':
                new_seat_map[i][j] = '#'
            else:
                new_seat_map[i][j] = c
            if data[i][j] != new_seat_map[i][j]:
                did_not_change &= False
    return new_seat_map, not did_not_change
    
    

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    
    print(part_1(data))
    # > 2270