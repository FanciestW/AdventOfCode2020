import os
from typing import List

def read_file(file_name: str) -> List[str]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            data.append(line.replace(' ', ''))
        return data
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(data)
