import os
from typing import List

def read_file(file_name: str) -> List[int]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                data.append(int(line.strip()))
        return data    
    except Exception as e:
        print(str(e))

def count_jolt_diff(data: List[int]) -> int:
    data.sort()
    print(data) # TODO::Remove me
    
    j1_count = 0
    j3_count = 0
    last_adapter = 0 # Wall socket starts at 0 jolts
    for n in data:
        jolt_diff = n - last_adapter
        if jolt_diff == 1:
            j1_count += 1
        elif jolt_diff == 3:
            j3_count += 1
        else:
            print(f'Last Adapter: {last_adapter}J, Bad Adapter: {n}J')
        last_adapter = n
    j3_count += 1 # Device adapter is always 3 jolt difference
    return j1_count * j3_count

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(count_jolt_diff(data))
    # > 1890