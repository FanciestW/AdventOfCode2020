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
    count = 0
    i = 0
    j = 0
    while(i < len(data)):
        if data[i][j] == '#':
            count += 1
        i += 1
        j += 3
        if (i >= len(data)): break
        if (j >= len(data[i])):
            j -= len(data[i])
    return count
    
data = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
print(check_trees(data))
