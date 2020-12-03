import os

def read_input(file_name: str) -> list:
    try:
        data = []
        read_file = open(file_name, 'r')
        while(True):
            line = read_file.readline()
            if not line:
                break
            data.append(list(line.strip()))
        return data
    except Exception as e:
        print(f'Error occurred: {e}')

def check_trees(data: list) -> int:
    pass
    
data = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
print(check_trees(data))
