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

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
