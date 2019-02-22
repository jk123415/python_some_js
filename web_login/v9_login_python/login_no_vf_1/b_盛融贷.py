import sys
sys.path.append("../..")
from no_vf_login import login


confi = {
    'name': '盛融贷',
    'cookies_path': ['D:\\火车采集器V9\\Data\\Cookie\\1613.txt'],
    'url': 'https://www.shengrongdai.com/loginAndRegiste/login.html',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="mobile"]',
    'password_selector': '//*[@id="password"]',
    'username': '15982657662',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login"]',
}

if __name__ == '__main__':
    login(confi)
