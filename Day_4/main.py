import os
import re

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

def check_passport_fields(passport: dict) -> bool:
    try:
        byr = int(passport['byr']) if re.match('^[0-9]{4}$', passport['byr']) else -1
        iyr = int(passport['iyr']) if re.match('^[0-9]{4}$', passport['iyr']) else -1
        eyr = int(passport['eyr']) if re.match('^[0-9]{4}$', passport['eyr']) else -1
        hgt_unit = passport['hgt'][-2:]
        hgt = int(passport['hgt'][:-2]) if passport['hgt'][:-2].isnumeric() else -1
        
        if byr < 1920 or byr > 2002:
            return False
        if iyr < 2010 or byr > 2020:
            return False
        if eyr < 2020 or eyr > 2030:
            return False
        if hgt_unit != 'in' and hgt_unit != 'cm':
            return False
        elif (hgt_unit == 'in' and (hgt <= 59 or hgt > 76)) or (hgt_unit == 'cm' and (hgt <= 150 or hgt > 193)):
            return False
        if not re.match('^[#]{1}[a-f0-9]{6}$', passport['hcl']):
            return False
        if not re.match('^((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)){1}$', passport['ecl']):
            return False
        if not re.match('^[0-9]{9}$', passport['pid']):
            return False
        
        return True
    except Exception as e:
        return False

def validate_passports(list_of_passports: list) -> int:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_count = 0
    for passport in list_of_passports:
        if all(f in passport for f in required_fields):
            valid_count += 1

    return valid_count

def validate_passports_v2(list_of_passports: list) -> int:
    valid_count = 0
    for passport in list_of_passports:
        if check_passport_fields(passport):
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(validate_passports(data))
    # > 182

    print(validate_passports_v2(data))
    # > 109
