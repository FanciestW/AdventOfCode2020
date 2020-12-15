import os
from typing import List, Tuple
import itertools

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
    addr_mask = int(mask.replace('1', '0').replace('0', '1').replace('X', '0'), 2)
    float_bits = [2**(len(mask) - 1 - i) for i, b in enumerate(mask) if b == 'X']
    addr_permutations = [0]
    for seq in [itertools.permutations(float_bits, i + 1) for i in range(0, len(float_bits))]:
        addr_permutations += [sum(list(i)) for i in seq]
    addr_permutations = list(set(addr_permutations))
    return bit_mask, addr_mask, addr_permutations

def init_memory_v2(data: List[str]) -> int:
    memory = dict()
    mask = 0
    addr_mask = 0
    addr_permutations = list()
    for instr_str in data:
        if 'mask' in instr_str:
            mask, addr_mask, addr_permutations = get_mask_data(instr_str[-36:])
        elif 'mem' in instr_str:
            num = int(instr_str[instr_str.index('=') + 2:].strip())
            mem_loc = int(instr_str[4:instr_str.index(']')])
            mem_loc |= mask
            mem_loc &= addr_mask
            mem_list = [mem_loc + p for p in addr_permutations]
            for m in mem_list:
                memory[m] = num
    return sum(memory.values())


if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(init_memory(data))
    # > 9967721333886

    print(init_memory_v2(data))
    # > 4355897790573