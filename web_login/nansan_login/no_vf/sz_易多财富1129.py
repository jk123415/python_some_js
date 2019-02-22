import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '易多财富',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\979.txt'],
    'url': 'https://www.11dd.cn/login/login.html',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="userName"]',
    'password_selector': '//*[@id="password"]',
    'username': 'minmin520',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginBt"]',
    'additional': ['time.sleep(1)', 'chrome.get(url)', 'time.sleep(2)']
}

if __name__ == '__main__':
    login(confi)
