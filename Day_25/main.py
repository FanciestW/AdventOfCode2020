import os

def read_file(filename: str) -> tuple:
    try:
        read_file = open(filename, 'r')
        num1 = int(read_file.readline().strip())
        num2 = int(read_file.readline().strip())
        return num1, num2
    except Exception as e:
        print(str(e))

def transform(subject_num: int, loop_size: int) -> int:
    value = 1 * subject_num
    for _ in range(1,loop_size):
        value *= subject_num
        value %= 20201227
    return value

def crack_loop_size(pub_key: int, subject_num=7) -> int:
    value = 1 * subject_num
    loop_size = 1
    while value != pub_key:
        value *= subject_num
        value %= 20201227
        loop_size += 1
    return loop_size

def part1(num1: int, num2: int) -> int:
    loop_size1 = crack_loop_size(num1)
    loop_size2 = crack_loop_size(num2)
    key1 = transform(num2, loop_size1)
    key2 = transform(num1, loop_size2)
    return key1 if key1 == key2 else None

if __name__ == '__main__':
    num1, num2 = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(part1(num1, num2))
    # > 8740494