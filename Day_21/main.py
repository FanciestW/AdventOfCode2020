import os
import re
from typing import List
import pprint

def read_file(file_name: str) -> List[tuple]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            ingredients = line[:line.index('(')].strip().split(' ')
            allergens = re.findall('\((.*?)\)', line)[0].replace('contains ', '').split(', ')
            data.append((ingredients, allergens))
        return data
    except Exception as e:
        print(str(e))

def build_data_struct(data: List[tuple]) -> (dict, list):
    ingredient_set = set()
    allergen_dict = dict()
    for ingredient_list, allergen_list in data:
        ingredient_set.update(ingredient_list)
        for allergen in allergen_list:
            if allergen in allergen_dict:
                allergen_dict[allergen].update(ingredient_list)
            else:
                allergen_dict[allergen] = set(ingredient_list)
    return allergen_dict, list(ingredient_set)

def find_no_allergens(allergen_dict: dict, ingredient_list: list) -> List[str]:
    allergen_list = allergen_dict.keys()
    unique_allergens = dict()
    for allergen in allergen_dict:
        for a in [a for a in allergen_list if a != allergen]:
            allergen_dict[allergen] = allergen_dict[allergen].difference(allergen_dict[a])
    print(unique_allergens)


if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'test_input.txt'))

    # Part 1:
    allergen_dict, ingredient_list = build_data_struct(data)
    pprint.pp(allergen_dict)
    pprint.pp(ingredient_list)
    no_allergens = find_no_allergens(allergen_dict, ingredient_list)
