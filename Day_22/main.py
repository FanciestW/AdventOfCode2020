import os
from typing import List

def read_file(file_name: str) -> (List[int], List[int]):
    try:
        p1_cards = list()
        p2_cards = list()
        read_file = open(file_name, 'r')
        isPlayer1 = True
        while True:
            line = read_file.readline()
            if not line:
                break
            else:
                line = line.strip()
            if 'Player 2' in line:
                isPlayer1 = False
            elif 'Player 1' in line:
                isPlayer1 = True
            elif isPlayer1 and line.isnumeric():
                p1_cards.append(int(line))
            elif not isPlayer1 and line.isnumeric():
                p2_cards.append(int(line))
        return (p1_cards, p2_cards)
    except Exception as e:
        print(str(e))

# Returns winning players score as int
def play_game(p1_cards: List[int], p2_cards: List[int]) -> int:
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        p1 = p1_cards.pop(0)
        p2 = p2_cards.pop(0)
        if p1 > p2:
            p1_cards += [p1, p2]
        elif p2 > p1:
            p2_cards += [p2, p1]
        else:
            print('A tie occurred')
    winner_cards = p1_cards if len(p1_cards) > 0 else p2_cards
    winning_sum = sum([(i + 1) * n for i, n in enumerate(winner_cards[::-1])])
    return winning_sum

if __name__ == '__main__':
    p1_cards, p2_cards = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))

    # Part 1:
    print(play_game(p1_cards, p2_cards))
    # > 32179