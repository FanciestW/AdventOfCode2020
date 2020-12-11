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

def count_valid_arrangements(data: List[int], start_j=0) -> int:
    data = [0] + sorted(data) + [max(data) + 3]
    path_count_list = [1] + [0 for i in data[1:]]
    print(data)
    for i in range(len(data)):
        if (data[i] + 1) in data[i:]:
            path_count_list[data.index(data[i] + 1)] += path_count_list[i]
        if (data[i] + 2) in data[i:]:
            path_count_list[data.index(data[i] + 2)] += path_count_list[i]
        if (data[i] + 3) in data[i:]:
            path_count_list[data.index(data[i] + 3)] += path_count_list[i]
    print(path_count_list)
    return path_count_list[-1]

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    print(count_jolt_diff(data))
    # > 1890

    print(count_valid_arrangements(data))