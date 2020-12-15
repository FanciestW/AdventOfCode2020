import os
from typing import List, Tuple

def read_file(file_name: str) -> List[str]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline().strip()
            if not line:
                break
            else:
                data.append(line)
        return data
    except Exception as e:
        print(str(e))

def get_bitmasks(mask: str) -> Tuple[int, int]:
    zero_mask = 0
    one_mask = 0
    for bit in mask:
        zero_mask <<= 1
        one_mask <<= 1
        if bit == '0':
            zero_mask |= 1
        elif bit == '1':
            one_mask |= 1
    return zero_mask, one_mask

def init_memory(data: List[str]) -> int:
    memory = dict()
    zero_mask = 0
    one_mask = 0
    for instr_str in data:
        if 'mask' in instr_str:
            zero_mask, one_mask = get_bitmasks(instr_str[-36:])
        elif 'mem' in instr_str:
            mem_loc = int(instr_str[4:instr_str.index(']')])
            mem_value = int(instr_str[instr_str.index('=') + 2:])
            mem_value |= one_mask
            mem_value &= ~zero_mask
            memory[mem_loc] = mem_value
    return sum(memory.values())

def get_mask_data(mask: str) -> Tuple[List[int], int]:
    bit_mask = int(mask.replace('X', '0'), 2)
    base_addr = bit_mask
    list_of_addr = [len(mask) - 1 - i for i, b in enumerate(mask) if b == 'X']
    # Find all memory addresses
    return bit_mask, list_of_addr

def init_memory_v2(data: List[str]) -> int:
    memory = dict()
    mask = 0
    for instr_str in data:
        if 'mask' in instr_str:
            mask = int(instr_str[-36:], 2)

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(init_memory(data))
    # > 9967721333886
