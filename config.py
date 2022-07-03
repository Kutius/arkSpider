import os
import datetime
import yaml


class Config:
    def __init__(self, config_file):
        # if file not exist, create it
        if not os.path.exists(config_file):
            with open(config_file, 'w', encoding='utf-8') as f:
                yaml.dump({}, f)

        # Load config file
        with open(config_file, encoding='utf-8') as f:
            __config = yaml.load(f, Loader=yaml.FullLoader)

        # Initialize config
        try:
            self.cookie = __config['cookie']
            self.token = __config['token']
        except TypeError:
            self.cookie = None
            self.token = None

    def setCookie(self, cookie):
        self.cookie = cookie
        self.__writeConfig()

    def setToken(self, token):
        self.token = token
        self.__writeConfig()

    def __writeConfig(self):
        __config = {
            'cookie': self.cookie,
            'token': self.token,
        }
        with open('config.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(__config, f)


def persist(data):
    now = datetime.datetime.now()
    fs_data = {'time': now, 'data': data}
    print(now)
    with open('./data.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(fs_data, f, encoding='utf-8', allow_unicode=True)


# Read data from data.yaml
def read_data():
    with open('./data.yaml', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data['data']
