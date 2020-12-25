import os
from typing import List

def read_file(filename: str) -> List[str]:
    try:
        data = list()
        read_file = open(filename, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            data.append(line)
        return data
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(data[:3])
