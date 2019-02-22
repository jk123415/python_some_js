import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '大盈家',
    'cookies_path': ['D:\\火车采集器V9\\Data\\Cookie\\1880.txt'],
    'url': 'http://www.dayingjia.net/webview/login.html',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': "//input[@id='username']",
    'password_selector': "//input[@id='userpwd']",
    'username': '13798495474',
    'password': 'minmin520',
    'submit_selector': "//button[@id='loginBtn']",
}

if __name__ == '__main__':
    login(confi)
