from utils import read_file_to_array


def scratch_cards(cards: dict):
    total = 0
    card_count = {k: 1 for k in cards.keys()}

    for k, v in cards.items():
        winners = set()
        i = 0
        while v[i] != '|':
            winners.add(v[i])
            i += 1

        winner_count = 0
        while i < len(v):
            if v[i] in winners and v[i]:
                winner_count += 1
            i += 1
        if winner_count > 0:
            total += 2 ** (winner_count - 1)
            for i in range(winner_count):
                card_count[k + i + 1] += card_count[k]

    return total, sum(card_count.values())


if __name__ == '__main__':
    x = read_file_to_array('inputs/day4.txt')
    card_dict = {}
    for i, card in enumerate(x, start=1):
        card_dict[i] = card.replace(f'Card {i}: ', '').split(' ')

    easy, hard = scratch_cards(card_dict)
    print(f'Easy: {easy}')
    print(f'Hard: {hard}')
