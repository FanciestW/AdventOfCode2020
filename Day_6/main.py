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
                temp_str_list.append(line.strip())
        if len(temp_str_list) > 0:
            data.append(temp_str_list)
        return data
    except Exception as e:
        print(str(e))

def sum_unique_questions(questions: list[str]) -> int:
    question_str = ''.join(q for q in questions)
    return len(list(set(question_str)))

def sum_all_yes_questions(question_str: str) -> int:
    question_dict = dict()
    for c in question_str:
        if c in question_dict:
            question_dict[c] += 1
        else:
            question_dict[c] = 1
    largest = None
    for key in question_dict.keys():
        if largest is None or question_dict[key] > question_dict[largest]:
            largest = key
    print(largest)
    return question_dict[largest]


if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(sum([sum_unique_questions(questions) for questions in data]))
    # > 6683

    # print(sum_all_yes_questions(data[1]))