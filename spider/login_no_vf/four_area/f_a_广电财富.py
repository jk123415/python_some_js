import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '广电财富',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\237.txt'],
    'url': 'https://www.guangdiancaifu.com/login',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '//*[@id="tx"]',
    'username_selector': '//*[@id="username"]',
    'password_selector': '//*[@id="password"]',
    'username': 'minmin520',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login-btn"]',
}

if __name__ == '__main__':
    login(confi)
