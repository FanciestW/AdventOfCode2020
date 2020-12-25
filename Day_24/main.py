import os
import re
from typing import List

def read_file(filename: str) -> List[List[str]]:
    try:
        data = list()
        read_file = open(filename, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            data.append(re.findall('[ns][ew]{1}|[ew]{1}', line))
        return data
    except Exception as e:
        print(str(e))

def part1(data: List[List[str]]) -> int:
    tiles = dict()
    for line in data:
        x, y = 0, 0
        for dir in line:
            if dir == 'e':
                x += 2
            elif dir == 'se':
                x += 1
                y -= 1
            elif dir == 'sw':
                x -= 1
                y -= 1
            elif dir == 'w':
                x -= 2
            elif dir == 'nw':
                x -= 1
                y += 1
            elif dir == 'ne':
                x += 1
                y += 1
        pos = f'{x},{y}'
        if pos in tiles:
            tiles[pos] = not tiles[pos]
        else:
            tiles[pos] = True
    return list(tiles.values()).count(True)


if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(part1(data))
