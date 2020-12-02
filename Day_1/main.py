import os

def read_input(file_name: str) -> list[int]:
    try:
        read_file = open(file_name, 'r')

        data = []
        while(True):
            line = read_file.readline().strip()
            if not line:
                break
            data.append(int(line))
        read_file.close()

        return data
    except Exception as e:
        print(f'An error occurred: {e}')

def report_repair(target: int) -> int:
    num_map = dict()
    nums = read_input(os.path.join(os.path.dirname(__file__), 'input1.txt'))
    for n in nums:
        if n in num_map:
            num_map[n] += 1
        else:
            num_map[n] = 1
    
    for n in nums:
        find_num = target - n
        if find_num in num_map:
            return find_num * n
    return None

def report_repair_v2(target: int) -> int:
    num_map = dict()
    nums = read_input(os.path.join(os.path.dirname(__file__), 'input1.txt'))
    for n in nums:
        if n in num_map:
            num_map[n] += 1
        else:
            num_map[n] = 1
    
    for i, n in enumerate(nums):
        for j, m in enumerate(nums):
            if i != j and (n + m) < 2020:
                find_num = 2020 - (n + m)
                if find_num in num_map:
                    return find_num * n * m
                else:
                    continue
            else:
                continue
    return None

print(report_repair(2020))
# > 1019571

print(report_repair_v2(2020))
# > 100655544
