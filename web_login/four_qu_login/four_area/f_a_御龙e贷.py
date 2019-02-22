import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '御龙e贷',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\1284.txt',
                     'E:\\4区火车头20160326\\Data\\Cookie\\627.txt'],
    'url': 'https://www.yulongdai.com/loginAndRegiste/login.html',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="mobile"]',
    'password_selector': '//*[@id="password"]',
    'username': '15817415369',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login"]',
}

if __name__ == '__main__':
    login(confi)
