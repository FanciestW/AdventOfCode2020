import os

def read_file(file_name: str) -> list[str]:
    try:
        data = []
        temp_str = ''
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            if line.strip() == '':
                data.append(temp_str)
                temp_str = ''
            else:
                temp_str += line.strip()
        if len(temp_str) > 0:
            data.append(temp_str)
        return data
    except Exception as e:
        print(str(e))

def sum_unique_questions(question_str: str) -> int:
    return len(list(set(question_str)))

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(sum([sum_unique_questions(question_str) for question_str in data]))
    # > 6683