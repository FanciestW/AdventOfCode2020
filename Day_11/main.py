import os
from typing import List

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

def part_1(data: List[List[str]]):
    neighbor_count = [[0 if c == 'L' else -1 for c in row] for row in data]
    print(neighbor_count)

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    print(data)