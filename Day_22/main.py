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

if __name__ == '__main__':
    p1_cards, p2_cards = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(p1_cards)
    print(p2_cards)