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

def check_instructions(instruction_list: list, start_num: int) -> bool:
    i = start_num
    while i < len(instruction_list):
        instr, num = instruction_list[i]
        if instr == 'done':
            return False
        elif instr == 'acc' or instr == 'nop':
            i += 1
        elif instr == 'jmp':
            i += num
    return True

def get_fixed_accumulator(instruction_list: list) -> int:
    accumulator = 0
    changed_one = False
    i = 0
    while i < len(instruction_list):
        instr, num = instruction_list[i]
        # Mark instruction as 'Done'
        temp_instr = list(instruction_list[i])
        temp_instr[0] = 'done'
        instruction_list[i] = tuple(temp_instr)
        if (instr == 'acc'):
            accumulator += num
            i += 1
        elif (instr == 'jmp'):
            if not changed_one and check_instructions(instruction_list, i + 1):
                i += 1
                changed_one = True
            else:
                i += num 
        elif (instr == 'nop'):
            if num != 0:
                if not changed_one and check_instructions(instruction_list, i + num):
                    i += num
                    changed_one = True
                else:
                    i += 1
            else:
                i += 1
        elif (instr == 'done'):
            break
        else:
            print(f'Instruction `{instr}` not known')
            break
    return accumulator

if __name__ == '__main__':
    data = read_data(os.path.join(os.path.dirname(__file__), 'input.txt'))
    # print(find_accumulator_before_loop(data))
    # > 1610

    print(get_fixed_accumulator(data))
