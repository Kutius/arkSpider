from login import token_api, login
from cards import convert_cards
from config import Config, persist


# Get token from cookie or config.yaml
def get_token():
    config = Config('config.yaml')
    if config.token is None:
        if config.cookie is not None:
            cookie = config.cookie
            token = token_api(cookie)
        else:
            print('No config, Please login first')
            phone = input('Please input your phone:')
            pwd = input('Please input your password:')
            token = login(phone, pwd)

        config.setToken(token)
    else:
        print('Read config token')
        token = config.token

    return token


def run():
    token = get_token()
    cards = convert_cards(token)
    persist(cards)
    # print(list(filter(lambda x: x['isNew'], cards)))

    print('token is: ', token)


if __name__ == '__main__':
    run()
