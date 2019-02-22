import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '润银所',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\1393.txt'],
    'url': 'https://www.runyinsuo.com/loginAndRegiste/login.html',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="mobile"]',
    'password_selector': '//*[@id="password"]',
    'username': '18078191783',
    'password': 'minmin520',
    'submit_selector': '//*[contains(@value,"登")]',
    'haveAlert': False,
    'wait_time': 1

}

if __name__ == '__main__':
    login(confi)
