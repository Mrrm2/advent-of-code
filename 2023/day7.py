from collections import Counter
from utils import read_file_to_array


def replace_letters(hand: list) -> list:
    mapping = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'}
    hand = ([mapping.get(hand[i], hand[i]) for i in range(len(hand))])

    return hand


def strength_map(hand: list) -> tuple:
    cards = Counter(hand)
    relative_strength = {(4, 1): 5, (3, 2): 4, (3, 1): 3, (2, 2): 2, (2, 1): 1, (1, 1): 0}
    ordered_hand = cards.most_common()
    if len(ordered_hand) == 1:
        strength = 6
    else:
        big2 = ordered_hand[0][1], ordered_hand[1][1]
        strength = relative_strength[big2]

    return strength, hand


def easy(rounds: list):
    ranking = []
    total = 0
    for round in rounds:
        hand, bet = round.split()
        hand = replace_letters(hand)
        ranking.append((hand, int(bet)))

    ranking.sort(key=lambda play: strength_map(play[0]))
    for rank, (_, bet) in enumerate(ranking, start=1):
        total += rank * bet

    return total


def replace_letters_hard(hand: list) -> list:
    mapping = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': '.', 'T': 'A'}
    hand = ([mapping.get(hand[i], hand[i]) for i in range(len(hand))])

    return hand


def strength_map_hard(hand: list) -> tuple:
    cards = Counter(hand)
    relative_strength = {(4, 1): 5, (3, 2): 4, (3, 1): 3, (2, 2): 2, (2, 1): 1, (1, 1): 0}
    ordered_hand = cards.most_common()
    if cards.get('.'):  # can be cleaned
        if len(ordered_hand) > 1:
            if ordered_hand[0][0] == '.':
                cards[ordered_hand[1][0]] += cards.get('.')
            else:
                cards[ordered_hand[0][0]] += cards.get('.')
        else:
            cards['E'] = 5
        del cards['.']
        ordered_hand = cards.most_common()

    if len(ordered_hand) == 1:
        strength = 6
    else:
        big2 = ordered_hand[0][1], ordered_hand[1][1]
        strength = relative_strength[big2]
    return strength, ''.join(hand)


def hard(rounds: list):
    ranking = []
    total = 0
    for round in rounds:
        hand, bet = round.split()
        hand = replace_letters_hard(hand)
        ranking.append((hand, int(bet)))

    ranking.sort(key=lambda play: strength_map_hard(play[0]))
    for rank, (_, bet) in enumerate(ranking, start=1):
        total += rank * bet

    return total


if __name__ == '__main__':
    file = read_file_to_array('inputs/day7.txt')
    print(f'Easy: {easy(file)}')
    print(f'Hard: {hard(file)}')

