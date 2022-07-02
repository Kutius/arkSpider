import yaml
import os


class Config:
    def __init__(self, config_file):
        # if file not exist, create it
        if not os.path.exists(config_file):
            with open(config_file, 'w', encoding='utf_8') as f:
                yaml.dump({}, f)

        # Load config file
        with open(config_file, encoding='utf_8') as f:
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
        with open('config.yaml', 'w', encoding='utf_8') as f:
            yaml.dump(__config, f)


if __name__ == '__main__':
    config = Config('config.yaml')
    print(config.config)
