import os

def read_input(file_name: str) -> list[str]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while(True):
            line = read_file.readline()
            if not line:
                break
            data.append(line.strip())
        return data
    except Exception as e:
        print(f'Error occurred: {e}')

def parse_password_line(pw_line: str) -> list:
    dash_index = pw_line.index('-')
    first_space_index = pw_line.index(' ')
    colon_index = pw_line.index(':')
    min_val = int(pw_line[:dash_index])
    max_val = int(pw_line[dash_index+1:first_space_index])
    letter = pw_line[first_space_index:colon_index].strip()
    password = pw_line[colon_index+1:].strip()
    return [min_val, max_val, letter, password]

def check_password(pw_line: str) -> bool:
    min_val, max_val, letter, password = parse_password_line(pw_line)
    # print(f'Min:{min_val}\tMax:{max_val}\tLetter:{letter}\tPassword:{password}')

    letter_count = 0
    for c in password:
        if c == letter:
            letter_count += 1

    return True if letter_count >= min_val and letter_count <= max_val else False

def check_password_v2(pw_line: str) -> bool:
    min_val, max_val, letter, password = parse_password_line(pw_line)
    if min_val > len(password) or max_val > len(password):
        return False
    return (password[min_val-1] == letter) ^ (password[max_val-1] == letter)

'''
Takes a list of password policies as a string and prints the valid password counts.
'''
def check_list_of_password(pw_list: list[str]) -> None:
    countv1 = 0
    countv2 = 0
    for pw in pw_list:
        if check_password(pw):
            countv1 += 1
        if check_password_v2(pw):
            countv2 += 1
    print(f'Version 1 Valid Passwords: {countv1}')
    print(f'Version 2 Valid Passwords: {countv2}')

data = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
check_list_of_password(data)
# > 620
# > 727