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

def hasPair(nums: List[int], target: int) -> bool:
    for i, n in enumerate(nums):
        target_num = target - n
        new_list = nums[:i] + nums[i+1:]
        if target_num in new_list:
            return True
    return False

def find_invalid_num(data: List[int], pre_count=25) -> int:
    for i in range(pre_count, len(data)):
        num = data[i]
        preamble_data = data[i-pre_count:i]
        if not hasPair(preamble_data, num):
            return num
    return None

def find_consecutive_nums(data: List[int], target_num: int) -> List[int]:
    for i, n in enumerate(data[:data.index(target_num):]):
        if n >= target_num:
            continue
        j = i + 2
        while j < len(data):
            data_subset = data[i:j]
            subset_sum = sum(data_subset)
            if subset_sum < target_num:
                j += 1
            elif subset_sum == target_num:
                return data_subset
            else:
                break

    return None

if __name__ == '__main__':
    data = read_data(os.path.join(os.path.dirname(__file__), 'input.txt'))
    invalid_num = find_invalid_num(data, pre_count=25)
    print(invalid_num)
    # > 2089807806

    consecutive_list = find_consecutive_nums(data, invalid_num)
    print(min(consecutive_list) + max(consecutive_list))
    # > 245848639

