from login import token_api, login
from config import Config


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

    print('token is: ', token)


if __name__ == '__main__':
    # user_info(TOKEN)

    run()
