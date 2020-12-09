import os
import copy

def read_data(file_name: str) -> list:
    try:
        data = []
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            instruction, instruction_number = line.split(' ')
            instruction_number = int(instruction_number)
            data.append((instruction, instruction_number))
        return data
    except Exception as e:
        print(str(e))

def find_accumulator(instruction_list: list) -> (int, bool):
    accumulator = 0
    i = 0
    seen_i = set()
    while i < len(instruction_list):
        if i in seen_i:
            return accumulator, False
        else:
            seen_i.add(i)
        instr, num = instruction_list[i]
        if instr == 'acc':
            accumulator += num
            i += 1
        elif instr == 'jmp':
            i += num
        elif instr == 'nop':
            i += 1
    return accumulator, True

def get_fixed_accumulator(instruction_list: list) -> int:
    i = 0
    while i < len(instruction_list):
        instr, num = instruction_list[i]
        if instr == 'jmp':
            new_instr = ('nop', num)
            instruction_list[i] = new_instr
        elif instr == 'nop':
            new_instr = ('jmp', num)
            instruction_list[i] = new_instr
        accum_res, hasNoCycles = find_accumulator(instruction_list)
        if hasNoCycles:
            return accum_res
            break
        else:
            instruction_list[i] = (instr, num)
            i += 1
    return None


if __name__ == '__main__':
    data = read_data(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(find_accumulator(data)[0])
    # > 1610

    print(get_fixed_accumulator(data))
    # > 1703
