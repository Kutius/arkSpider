import requests

TOKEN = 'eLFmOwKRXR1IQlvrOZ406NU1'


# Login by phone and password
def login(phone, pwd):
    login_url = "https://as.hypergryph.com/user/auth/v1/token_by_phone_password"
    data = {"phone": phone, "password": pwd}
    res = requests.post(login_url, data=data)
    if res.status_code != 200:
        raise Exception('Login failed')

    return res.json()['data']['token']


# User information
def user_info(token):
    user_url = 'https://as.hypergryph.com/u8/user/info/v1/basic'
    data = {
        "appId": 1,
        "channelMasterId": 1,
        "channelToken": {
            'token': token
        },
    }
    res = requests.post(user_url, json=data)
    if res.status_code != 200:
        raise Exception('Get user info failed')

    account = {
        'uid': res.json()['data']['uid'],
        'nickName': res.json()['data']['nickName'],
    }
    return account


# Get token by cookie
def token_api(cookie):
    token_url = "https://web-api.hypergryph.com/account/info/hg"
    header = {'cookie': cookie}
    res = requests.get(token_url, headers=header)
    token = res.json()['data']['content']

    return token
