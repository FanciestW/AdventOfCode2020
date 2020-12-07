import os

def read_file(file_name: str) -> list:
    try:
        data = []
        temp_str_list = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            if line.strip() == '':
                data.append(temp_str_list)
                temp_str_list = []
            else:
                temp_str_list.append(''.join(sorted(line.strip())))
        if len(temp_str_list) > 0:
            data.append(temp_str_list)
        return data
    except Exception as e:
        print(str(e))

def sum_unique_questions(questions: list[str]) -> int:
    question_str = ''.join(q for q in questions)
    return len(list(set(question_str)))

def sum_all_yes_questions(questions: list[str]) -> int:
    unique_questions = list(set(''.join(q for q in questions)))
    count = 0
    for c in unique_questions:
        if all(c in question for question in questions):
            count += 1
    return count


if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    pass
    print(sum([sum_unique_questions(questions) for questions in data]))
    # > 6683

    print(sum([sum_all_yes_questions(questions) for questions in data]))
    # > 3122