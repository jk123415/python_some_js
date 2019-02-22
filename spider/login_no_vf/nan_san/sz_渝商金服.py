import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '渝商金服',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1076.txt'],
    'url': 'https://www.ysjrfw.com/login/login',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="login_form"]/div[1]/div[1]/input',
    'password_selector': '//*[@id="passwords"]',
    'username': '13421464186',
    'password': 'minmin520',
    'submit_selector': '//*[@id="submit-a"]',
    'additional_cookie': []
}

if __name__ == '__main__':
    login(confi)
