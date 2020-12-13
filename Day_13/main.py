import os
import math
from typing import List, Tuple
from functools import reduce

def read_file(file_name: str) -> Tuple[int, List[int]]:
    try:
        time = 0
        bus_ids = list()
        read_file = open(file_name, 'r')
        time = int(read_file.readline().strip())
        bus_ids = [(i, int(n)) for i, n in enumerate(read_file.readline().strip().split(',')) if n.isnumeric()]
        return (time, bus_ids)
    except Exception as e:
        print(str(e))

def get_wait_time(time: int, bus_id: int) -> int:
    return (math.ceil(time / bus_id) * bus_id) - time

def find_best_bus(time: int, bus_ids: List[int]) -> int:
    bus_times = {id: get_wait_time(time, id) for id in bus_ids}
    best_bus = min(bus_times, key=bus_times.get)
    return bus_times[best_bus] * best_bus

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part_2(bus_ids: List[int]) -> int:
    buses = [bus_id for _, bus_id in bus_ids]
    positions = [bus_id - i for i, bus_id in bus_ids]
    return chinese_remainder(buses, positions)

if __name__ == '__main__':
    time, bus_ids = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(find_best_bus(time, [id for _, id in bus_ids]))
    # > 203

    print(part_2(bus_ids))
    # > 905694340256752