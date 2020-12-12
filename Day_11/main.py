import os
from typing import List, Tuple
import itertools
import copy
import numpy as np

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
    while did_change:
        seating, did_change = seat_move(seating)
    return [c for row in seating for c in row].count('#')
    
def seat_move(data: List[List[str]]) -> Tuple[List[List[str]], bool]:
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

def seat_move_v2(data: np.ndarray) -> Tuple[np.ndarray, bool]:
    new_seat_map = np.copy(data)
    did_not_change = True
    for x, row in enumerate(data):
        for y, c in enumerate(row):
            if c not in ['L', '#']:
                new_seat_map[x][y] = '.'
                continue
            top = data[:x, y]
            bottom = data[x+1:, y]
            left = data[x, :y]
            right = data[x, y+1:]
            top_left_diag = np.diagonal(data[:x,:y], offset=1 if y % 2 == 1 else 0)
            top_right_diag = np.diagonal(np.fliplr(data[:x,y+1:]), offset=1 if (len(row) - y - 1) % 2 == 1 else 0)
            bottom_left_diag = np.diagonal(np.flipud(data[x+1:,:y]))
            bottom_right_diag = np.diagonal(data[x+1:,y+1:])
            if (x > 3 and y > 3):
                print(data[:x,y+1:])
                print(top_left_diag)
                print(top_right_diag)
                print(bottom_left_diag) 
                print(bottom_right_diag)
            continue

def part_2(data: List[List[int]]):
    seating = np.array(data)
    did_change = True
    while did_change:
        seating, did_change = seat_move_v2(seating)
    return [c for row in seating for c in row].count('#')
    

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    
    # print(part_1(data))
    # > 2270

    part_2(data)