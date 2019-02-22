import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '渝商宝',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1096.txt'],
    'url': 'https://www.yjb666.com/login/login',
    'headless': True,
    'bf_username_click': '//*[@id="loginForm"]/div[1]/label',
    'bf_password_click': '',
    'username_selector': '//*[@id="loginForm"]/div[1]/input',
    'password_selector': '//*[@id="loginForm"]/div[2]/input',
    'username': 'minmin520',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginForm"]/div[6]/button',
    'additional_cookie': []
}

if __name__ == '__main__':
    login(confi)
