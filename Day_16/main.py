import os
from typing import List
import numpy as np

def read_file(file_name: str) -> list():
    try:
        known_values = dict()
        ticket_data = list()
        other_tickets = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            line = line.strip()
            if 'or' in line:
                values = [tuple([int(n) for n in d.strip().split('-')]) for d in line[line.index(':') + 1:].split('or')]
                known_values[line[:line.index(':')]] = values
            elif 'your ticket' in line:
                line = read_file.readline().strip()
                ticket_data = [int(n) for n in line.split(',')]
            elif ',' in line:
                other_tix_data = [int(n) for n in line.split(',')]
                other_tickets.append(other_tix_data)
        return known_values, ticket_data, other_tickets
    except Exception as e:
        print(str(e))
    
def find_invalid_sum(known: dict(), other_tickets: List[List[int]]) -> int:
    invalid_nums = list()
    nums = [n for tix_data in other_tickets for n in tix_data]
    for n in nums:
        valid = False
        for first_cond, second_cont in known.values():
            if (n >= first_cond[0] and n <= first_cond[1]) or (n >= second_cont[0] and n <= second_cont[1]):
                valid = True
                break
        if not valid:
            invalid_nums.append(n)
    return sum(invalid_nums)

def find_labels(known: dict, mytix: List[int], others: List[List[int]]) -> int:
    pass

if __name__ == '__main__':
    known, mytix, others = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(find_invalid_sum(known, others))
    # > 20048