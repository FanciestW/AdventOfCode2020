import os
from typing import List

def read_input(file_name: str) -> List[int]:
    try:
        read_file = open(file_name, 'r')
        return [int(n) for n in read_file.readline().strip().split(',')]
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    data = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(data)