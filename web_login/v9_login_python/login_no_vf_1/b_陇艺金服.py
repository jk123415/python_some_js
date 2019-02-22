import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '陇艺金服',
    'cookies_path': ['D:\\火车采集器V9\\Data\\Cookie\\1786.txt'],
    'url': 'https://www.longe360.com/login/login',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[contains(@name,"userName")]',
    'password_selector': '//*[@id="passwords"]',
    'username': '15982657662',
    'password': 'minmin520',
    'submit_selector': '//*[@id="submit-a"]',
}

if __name__ == '__main__':
    login(confi)
