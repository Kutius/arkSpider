import questionary

from login import token_api, login
from cards import convert_cards
from analysis import summary
from config import Config, persist, read_data


# Get token from cookie or config.yaml
def get_token():
    config = Config('config.yaml')
    if config.token is None:
        if config.cookie is not None:
            cookie = config.cookie
            token = token_api(cookie)
        else:
            print('❗No config, Please login first')
            user = questionary.form(
                phone=questionary.text('Please input your phone:'),
                pwd=questionary.password('Please input your password:')).ask()
            token = login(user.phone, user.pwd)

        config.setToken(token)
    else:
        print('Read config token')
        token = config.token

    return token


def run():
    choose = questionary.select(
        "How to get data?",
        choices=[
            "Default",
            "Local",
            "Cookie",
        ]).ask()
    match choose:
        case 'Default':
            token = get_token()
            cards = convert_cards(token)
            persist(cards)
            print('token is: ', token)
        case 'Local':
            cards = read_data()
        case 'Cookie':
            cookie = questionary.text('Please input your cookie:')
            token = token_api(cookie)
            cards = convert_cards(token)

    # print('Total 6🌟 cards: ', byRarity(cards))
    # per = summary(cards)
    # questionary.print(
    #     'On average, one six-star character is drawn for every '+ str(per),
    #     style='italic green')
    summary(cards)


if __name__ == '__main__':
    run()
