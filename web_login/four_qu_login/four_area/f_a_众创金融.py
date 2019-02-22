import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '众创金融',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\631.txt'],
    'url': 'https://www.zcrong.com/toLogin.do',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="userAccount"]',
    'password_selector': '//*[@id="password"]',
    'username': 'minmin520',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginHref"]',
    #'haveAlert': True,
    #'wait_time': 3

}

if __name__ == '__main__':
    login(confi)
