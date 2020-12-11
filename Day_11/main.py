import os
from typing import List

def read_file(file_name: str) -> List[List[int]]:
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

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(data)