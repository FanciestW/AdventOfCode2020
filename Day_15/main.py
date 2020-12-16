import os
import time
from typing import List

def read_input(file_name: str) -> List[int]:
    try:
        read_file = open(file_name, 'r')
        return [int(n) for n in read_file.readline().strip().split(',')]
    except Exception as e:
        print(str(e))

def part_1(data: List[int], number=2020) -> int:
    seen = dict()
    last_said = None
    for n in range(number):
        turn = n + 1
        i = n % len(data)
        num = data[i]
        if num not in seen:
            seen[num] = [turn]
            last_said = num
        elif last_said in seen:
            if len(seen[last_said]) < 2:
                last_said = 0
            else:
                last_said = abs(seen[last_said][1] - seen[last_said][0])
            if last_said in seen:
                seen[last_said].append(turn)
                if last_said in seen and len(seen[last_said]) > 2:
                    seen[last_said].pop(0)
            else:
                seen[last_said] = [turn]
            
        
            
    return last_said


if __name__ == '__main__':
    data = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    # part_1([0,3,6])
    print(part_1(data))
    # > 1294 

    start_time = time.time()
    print(part_1(data, number=30000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    # > 573522 (Took ~83 seconds)