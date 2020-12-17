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
    
def find_invalid_sum(known: dict(), other_tickets: List[List[int]]) -> tuple:
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
    return sum(invalid_nums), [tix for tix in others if not any(t in invalid_nums for t in tix)]

def check_conditions(n: int, cond1: tuple, cond2: tuple) -> bool:
    return (n >= cond1[0] and n <= cond1[1]) or (n >= cond2[0] and n <= cond2[1])

def find_labels(known: dict, mytix: List[int], others: List[List[int]]) -> int:
    complete_tix = dict()
    others_np = np.array(others)
    for i, col_data in enumerate(others_np.T):
        for key in known:
            cond1, cond2 = known[key]
            if all(check_conditions(n, cond1, cond2) for n in col_data) and key not in complete_tix:
                complete_tix[key] = mytix[i]
                break
    test = [complete_tix[key] for key in complete_tix if 'departure' in key]
    return sum(test)

if __name__ == '__main__':
    known, mytix, others = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    the_total, valid_tix = find_invalid_sum(known, others)
    print(the_total)
    # > 20048

    print(find_labels(known, mytix, valid_tix))