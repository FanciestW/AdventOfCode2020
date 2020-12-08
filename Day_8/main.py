import os

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

def find_accumulator_before_loop(instruction_list: list) -> int:
    accumulator = 0
    i = 0
    while i < len(instruction_list):
        instr, num = instruction_list[i]
        instruction_list[i] = ('done', 0)
        if (instr == 'acc'):
            accumulator += num
            i += 1
        elif (instr == 'jmp'):
            i += num
        elif (instr == 'nop'):
            i += 1
        elif (instr == 'done'):
            break
        else:
            print(f'Instruction `{instr}` not known')
            break
    return accumulator

if __name__ == '__main__':
    data = read_data(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(find_accumulator_before_loop(data))
    # > 1610
