import os 
from typing import List

def read_data(file_name: str) -> List[int]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            data.append(int(line))
        return data
    except Exception as e:
        print(str(e))

def check_rule(data: List[int], pre_count=25) -> int:
    for i in range(pre_count, len(data)):
        num = data[i]
        preamble_data = data[i-pre_count:i]
        print(i, preamble_data)

if __name__ == '__main__':
    data = read_data(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    check_rule(data, pre_count=5)