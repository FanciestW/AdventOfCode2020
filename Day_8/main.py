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

if __name__ == '__main__':
    data = read_data(os.path.join(os.path.dirname(__file__), 'test_input.txt'))
    print(data)
