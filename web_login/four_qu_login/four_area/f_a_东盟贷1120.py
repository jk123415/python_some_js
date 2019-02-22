import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '东盟贷',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\1423.txt'],
    'url': 'https://www.dongmengdai.com/index.php?user&q=action/login',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="keywords"]',
    'password_selector': '//*[@id="password"]',
    'username': 'minmin520',
    'password': 'minmin520',
    'submit_selector': '//*[contains(@value,"登录")]',
    'haveAlert': True,
    'wait_time': 3

}

if __name__ == '__main__':
    login(confi)
