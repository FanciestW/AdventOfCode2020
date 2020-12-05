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
        if len(temp_obj.keys()) > 0:
            data.append(temp_obj)
        return data
    except Exception as e:
        print(f'Error occurred: {e}')
        return []

def validate_passports(list_of_passports: list) -> int:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_fields = ['cid']
    valid_count = 0
    for passport in list_of_passports:
        if all(f in passport for f in required_fields):
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(validate_passports(data))
    # > 182
