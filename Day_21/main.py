import os
import re
from typing import List

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

def build_ingredient_dict(data: List[tuple]) -> dict:
    ingredient_allergen_dict = dict()
    for ingredient_list, allergen_list in data:
        for ingredient in ingredient_list:
            for allergen in allergen_list:
                if ingredient in ingredient_allergen_dict and allergen in ingredient_allergen_dict[ingredient]:
                    ingredient_allergen_dict[ingredient][allergen] += 1
                elif ingredient in ingredient_allergen_dict:
                    ingredient_allergen_dict[ingredient][allergen] = 1
                else:
                    ingredient_allergen_dict[ingredient] = { allergen: 1 }
    return ingredient_allergen_dict


if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'test_input.txt'))

    allergen_dict = build_ingredient_dict(data)
    print(allergen_dict)
