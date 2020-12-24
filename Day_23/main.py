def crab_cups(cycle, n=10):
    cur_val = cycle[0]
    max_val = max(cycle)

    cycle_dict = dict(zip(cycle, cycle[1:]))
    cycle_dict[cycle[-1]] = cycle[0]

    def pick_up(n=3):
        pick = [cycle_dict[cur_val]]
        for _ in range(n-1):
            pick.append(cycle_dict[pick[-1]])
        return pick

    for r in range(n):
        pick = pick_up()

        next_val = cur_val-1
        while next_val <= 0 or next_val in pick:
            next_val -= 1
            if next_val <= 0:
                next_val = max_val

        cycle_dict[cur_val] = cycle_dict[pick[-1]]
        cycle_dict[pick[-1]] = cycle_dict[next_val]
        cycle_dict[next_val] = pick[0]

        cur_val = cycle_dict[cur_val]

    return cycle_dict

## Part 1
cycle = crab_cups(
    [int(t) for t in list("135468729")], n=100)

result = [cycle[1]]
while result[-1] != 1:
    result.append(cycle[result[-1]])
print("".join([str(c) for c in result[:-1]]))

## Part 2
puzzle_input = [int(t) for t in list("135468729")]+list(range(9+1, 1000000+1))
cycle = crab_cups(puzzle_input, n=10000000)
v1 = cycle[1]
v2 = cycle[v1]
print(v1, v2, v1*v2)