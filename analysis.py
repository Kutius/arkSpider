def findByAttr(cards, value, attr='name'):
    lists = list(filter(lambda x: x[attr] == value, cards))
    return lists


def summary(cards):

    total = len(cards)
    rarity_5 = findByAttr(cards, 5, 'rarity')
    rarity_4 = findByAttr(cards, 4, 'rarity')

    print('Total: ', total)
    print('6🌟: ', len(rarity_5), ',They are:\n', get_name(rarity_5))
    print('5🌟: ', len(rarity_4), ',They are:\n', get_name(rarity_4))
    print('\n\n')

    # return total / len(rarity_5)


def get_name(cards):
    return list(map(lambda x: x['name'], cards))
