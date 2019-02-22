import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '乾安鑫',
    'cookies_path': ['D:\\火车采集器V9\\Data\\Cookie\\1851.txt'],
    'url': 'https://www.qiananxinchina.com/login/toLogin.do',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="userName"]',
    'password_selector': '//*[@id="passWord"]',
    'username': '18874240604',
    'password': 'minmin520',
    'submit_selector': '//*[@id="log"]',
}

if __name__ == '__main__':
    login(confi)
