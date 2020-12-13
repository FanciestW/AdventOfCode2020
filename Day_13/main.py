import os
from typing import List, Tuple

def read_file(file_name: str) -> Tuple[int, List[int]]:
    try:
        time = 0
        bus_ids = list()
        read_file = open(file_name, 'r')
        time = int(read_file.readline().strip())
        bus_ids = [int(n) for n in read_file.readline().strip().split(',') if n.isnumeric()]
        return (time, bus_ids)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    time, bus_ids = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(time, bus_ids)