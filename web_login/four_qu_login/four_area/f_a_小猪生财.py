import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '小猪生财',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\529.txt'],
    'url': 'https://www.pigcaifu.com/memberLoginPage',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="username"]',
    'password_selector': '//*[@id="password"]',
    'username': '15982657662',
    'password': 'minmin520',
    'submit_selector': '//*[@id="butt"]',
}

if __name__ == '__main__':
    login(confi)
