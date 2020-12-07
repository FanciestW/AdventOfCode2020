import os
import re

def read_file(file_name: str) -> dict:
    try:
        data = dict()
        read_file = open(file_name, 'r')

        while True:
            line = read_file.readline()
            if not line:
                break
            line = line.strip()
            main_bag = line[:line.index('bags contain') - 1]
            
            contained_bags = [s.strip('. ') for s in line[line.index('contain') + len('contain') + 1:].split(', ')]
            contained_bags_dict = dict()
            for bag in contained_bags:
                if 'no other' in bag:
                    contained_bags_dict = {}
                    break
                else:
                    quantity = int(re.match('(\d ){1}', bag)[0].strip())
                    bag = re.sub('(\d ){1}', '', bag)
                    color = re.sub('( bag[s]?){1}', '', bag)
                    contained_bags_dict[color] = quantity
                data[main_bag] = contained_bags_dict

        return data
    except Exception as e:
        print(str(e))
    
def find_bags_count(bags_dict: dict, target_color: str) -> int:
    found_bags = list()
    search_colors = [target_color]
    while len(search_colors) > 0:
        search = search_colors.pop()
        for bag in bags_dict:
            if bag in found_bags:
                continue
            elif any(c == search for c in list(bags_dict[bag].keys())):
                search_colors.append(bag)
                found_bags.append(bag)
    return len(found_bags)

def count_inner_bags(bags_dict: dict, target_color: str, root=True) -> int:
    bag_count = 0 if root else 1
    if target_color not in bags_dict:
        return bag_count
    for bag_color in bags_dict[target_color]:
        bag_count += (bags_dict[target_color][bag_color] * count_inner_bags(bags_dict, bag_color, root=False))
    return bag_count

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(find_bags_count(data, 'shiny gold'))
    # > 289

    print(count_inner_bags(data, 'shiny gold'))
    # > 30055