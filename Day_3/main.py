import os
import math

def read_input(file_name: str) -> list:
    try:
        data = []
        read_file = open(file_name, 'r')
        while(True):
            line = read_file.readline()
            if not line:
                break
            data.append(list(line.strip()))
        return data
    except Exception as e:
        print(f'Error occurred: {e}')

def check_trees(data: list) -> int:
    count = 0
    i = 0
    j = 0
    while(i < len(data)):
        if data[i][j] == '#':
            count += 1
        i += 1
        j += 3
        if (i >= len(data)): break
        if (j >= len(data[i])):
            j -= len(data[i])
    return count

def check_trees_v2(data: list, right_count: int, down_count: int) -> int:
    count = 0
    i = 0
    j = 0
    while(i < len(data)):
        if data[i][j] == '#':
            count += 1
        i += down_count
        j += right_count
        if (i >= len(data)): break
        if (j >= len(data[i])):
            j -= len(data[i])
    return count

# Part 1
data = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
print(check_trees(data))
# > 244

# Part 2
res_list = list()
res_list.append(check_trees_v2(data, 1, 1))
res_list.append(check_trees_v2(data, 3, 1))
res_list.append(check_trees_v2(data, 5, 1))
res_list.append(check_trees_v2(data, 7, 1))
res_list.append(check_trees_v2(data, 1, 2))
print(math.prod(res_list))
# > 9406609920
