import os
import math
from typing import List

def read_file(file_name: str) -> List[tuple]:
    try:
        data = []
        read_file = open(file_name, 'r')
        while True:
            line = read_file.readline().strip()
            if not line:
                break
            else:
                data.append((line[0], int(line[1:])))
        return data
    except Exception as e:
        print(str(e))

def pt1_move(instr: List[tuple]) -> int:
    forward_dict = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    ew_unit = 0
    ns_unit = 0
    facing = 90 # Direction in degrees (N = 0)
    for cmd, num in instr:
        if cmd == 'N' or (cmd == 'F' and forward_dict[facing] == 'N'):
            ns_unit += num
        elif cmd == 'S' or (cmd == 'F' and forward_dict[facing] == 'S'):
            ns_unit -= num
        elif cmd == 'E' or (cmd == 'F' and forward_dict[facing] == 'E'):
            ew_unit += num
        elif cmd == 'W' or (cmd == 'F' and forward_dict[facing] == 'W'):
            ew_unit -= num
        elif cmd == 'R':
            facing += num
        elif cmd == 'L':
            facing -= num
        # Normalize rotation to 0-360 degree.
        if facing <= -360 or facing >= 360:
            facing = facing % 360
        if facing < 0:
            facing = 360 + facing
    return abs(ew_unit) + abs(ns_unit)

def pt2_move(instr: List[tuple]) -> int:
    waypoint = [1, 10] # 1 unit North, 10 East. Negative values are south and west.
    ew_unit = 0
    ns_unit = 0

    for cmd, num in instr:
        if cmd == 'F':
            ns_unit += (waypoint[0] * num)
            ew_unit += (waypoint[1] * num)
        elif cmd == 'N':
            waypoint[0] += num
        elif cmd == 'S':
            waypoint[0] -= num
        elif cmd == 'E':
            waypoint[1] += num
        elif cmd == 'E':
            waypoint[1] -= num
        elif cmd in ['L', 'R']:
            rotate = num if cmd == 'R' else 360 - num
            ns_temp = waypoint[0]
            if rotate == 90:
                waypoint[0] = -1 * waypoint[1]
                waypoint[1] = ns_temp
            elif rotate == 180:
                waypoint[0] = -1 * ns_temp
                waypoint[1] = -1 * waypoint[1]
            elif rotate == 270:
                waypoint[0] = waypoint[1]
                waypoint[1] = -1 * ns_temp
    return abs(ew_unit) + abs(ns_unit)


if __name__ == '__main__':
    data = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(pt1_move(data))
    # > 2228

    print(pt2_move(data))
    # > 42908
