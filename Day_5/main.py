import os
import re

def read_file(file_name: str) -> list[str]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while(True):
            line = read_file.readline().strip()
            if not line:
                break
            if (re.match('^[FB]{7}[RL]{3}$', line)):
                data.append(line)
        return data
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
