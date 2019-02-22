import sys
sys.path.append("../..")
from no_vf_login import login


confi = {
    'name': '木牛流马',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\540.txt'],
    'url': 'http://www.mnlmjr.com/index.php?ctl=user&act=login',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="login-email-address"]',
    'password_selector': '//*[@id="login-password"]',
    'username': '15982657662',
    'password': 'minmin520',
    'submit_selector': '//*[@id="user-login-submit"]',
}

if __name__ == '__main__':
    login(confi)
