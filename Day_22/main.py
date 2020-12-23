import os
from typing import List
from math import prod

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

# Returns winning players score as int and a bool which is True if player 1 wins
def play_game(p1_cards: List[int], p2_cards: List[int], recursive_mode=True) -> (int, bool):
    p1_seen_set = set()
    p2_seen_set = set()
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        p1_deck, p2_deck = tuple(p1_cards), tuple(p2_cards)
        if p1_deck in p1_seen_set or p2_deck in p2_seen_set:
            return (-1, True)
        else:
            p1_seen_set.add(p1_deck)
            p2_seen_set.add(p2_deck)

        p1 = p1_cards.pop(0)
        p2 = p2_cards.pop(0)
        p1_win = False
        if recursive_mode and (p1 <= len(p1_cards) and p2 <= len(p2_cards)):
            p1_win = play_game(p1_cards[:p1], p2_cards[:p2], recursive_mode=True)[1]
        else:
            p1_win = p1 > p2

        if p1_win:
            p1_cards += [p1, p2]
        else:
            p2_cards += [p2, p1]
    p1_win = len(p1_cards) > 0
    winner_cards = p1_cards if len(p1_cards) > 0 else p2_cards
    return sum([(i + 1) * n for i, n in enumerate(winner_cards[::-1])]), p1_win

if __name__ == '__main__':
    p1_cards, p2_cards = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))

    # Part 1:
    print(play_game(p1_cards, p2_cards, recursive_mode=False)[0])
    # > 32179

    # Part 2:
    print(play_game(p1_cards, p2_cards, recursive_mode=True)[0])
    # > 30498