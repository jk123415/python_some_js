import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '1+2金融',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1071.txt'],
    'url': 'https://www.12money.cn/login.do',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '//*[@id="loginPassword"]',
    'username_selector': '//*[@id="loginName"]',
    'password_selector': '//*[@id="loginPasswordShow"]',
    'username': '13421464186',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginButton"]',
}

if __name__ == '__main__':
    login(confi)
