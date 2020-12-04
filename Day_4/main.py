import os

def read_file(file_name: str) -> list:
    try:
        data = list()
        temp_obj = dict()
        read_file = open(file_name, 'r')
        while(True):
            line = read_file.readline()
            if not line:
                break
            elif line == '\n':
                data.append(temp_obj)
                temp_obj = {}
                continue
            else:
                for data_field in line.strip().split(' '):
                    key, value = data_field.split(':')
                    temp_obj[key] = value
        return data
    except Exception as e:
        print(f'Error occurred: {e}')
        return []

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(data[0])
    print(data[1])