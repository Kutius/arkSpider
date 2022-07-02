import requests


def get_cards(token, page='1'):
    url = 'https://ak.hypergryph.com/user/api/inquiry/gacha?page='\
          + page +'&token=' + token + '&channelId=1'
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Get cards failed')

    return res.json()['data']


# Extract information for each piece of list
def process_cards(lists):
    cards = []

    for li in lists:
        for char in li['chars']:
            cards.append({
                'ts': li['ts'],
                'pool': li['pool'],
                'name': char['name'],
                'rarity': char['rarity'],
                'isNew': char['isNew'],
            })

    return cards


# Analyze cards
def analyze_cards(token):
    cards = []
    pagination = get_cards(token)['pagination']
    while pagination['current'] <= pagination['total']:
        # Get cards list
        lists = get_cards(token, str(pagination['current']))['list']
        cards.extend(process_cards(lists))
        pagination['current'] += 1

    return cards
