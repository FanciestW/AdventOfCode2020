import os
import re
from typing import List

def read_file(file_name: str) -> List[str]:
    try:
        data = list()
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            data.append(line)
        return data
    except Exception as e:
        print(str(e))

def eval_equation(eq: str) -> int:
    try:
        eq = eq.replace(' ', '')
        if eq.count('(') != eq.count(')'):
            raise ValueError('Bad parentheses!')
        while eq.count('(') > 0:
            stack = list()
            for i, c in enumerate(eq):
                if c == '(':
                    stack.append(i)
                elif c == ')':
                    start_i = stack.pop() + 1
                    end_i = i
                    inner_eq = eq[start_i:end_i]
                    inner_res = str(eval_equation(inner_eq))
                    eq = eq.replace(f'({inner_eq})', inner_res, 1)
                    break
        # No more inner equations wrapped in parentheses:
        while eq.count('*') > 0 or eq.count('+') > 0:
            eval_str = re.findall('(\d+[*+]{1}\d+)', eq)[0]
            eval_res = eval(eval_str)
            eq = eq.replace(eval_str, str(eval_res), 1)
        return int(eq)
    except Exception as e:
        print(str(e))

def part_1(data: List[str]) -> None:
    eval_res = [eval_equation(eq) for eq in data]
    print(sum(eval_res))


def eval_equation_v2(eq: str) -> int:
    try:
        eq = eq.replace(' ', '')
        if eq.count('(') != eq.count(')'):
            raise ValueError('Bad parentheses!')
        while eq.count('(') > 0:
            stack = list()
            for i, c in enumerate(eq):
                if c == '(':
                    stack.append(i)
                elif c == ')':
                    start_i = stack.pop() + 1
                    end_i = i
                    inner_eq = eq[start_i:end_i]
                    inner_res = str(eval_equation_v2(inner_eq))
                    eq = eq.replace(f'({inner_eq})', inner_res, 1)
                    break
        # No more inner equations wrapped in parentheses:
        while eq.count('+') > 0:
            eval_str = re.findall('(\d+[+]{1}\d+)', eq)[0]
            eval_res = eval(eval_str)
            eq = eq.replace(eval_str, str(eval_res), 1)
        while eq.count('*') > 0:
            eval_str = re.findall('(\d+[*]{1}\d+)', eq)[0]
            eval_res = eval(eval_str)
            eq = eq.replace(eval_str, str(eval_res), 1)
        return int(eq)
    except Exception as e:
        print(str(e))

def part_2(data: List[str]) -> None:
    eval_res = [eval_equation_v2(eq) for eq in data]
    print(sum(eval_res))

if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    part_1(data)
    # > 5783053349377

    part_2(data)
    # > 74821486966872
