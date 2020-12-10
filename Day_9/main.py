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

def check_rule(data: List[int], pre_count=25) -> int:
    for i in range(pre_count, len(data)):
        num = data[i]
        preamble_data = data[i-pre_count:i]
        if not hasPair(preamble_data, num):
            return num
    return None


if __name__ == '__main__':
    data = read_data(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(check_rule(data, pre_count=25))
    # > 2089807806