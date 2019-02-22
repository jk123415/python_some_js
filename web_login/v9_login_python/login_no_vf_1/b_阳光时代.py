import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '阳光时代',
    'cookies_path': ['D:\\火车采集器V9\\Data\\Cookie\\1764.txt'],
    'url': 'https://www.sunshinep2p.com/loginAndRegiste/login.html',
    'headless': False,
    'bf_username_click': "",
    'bf_password_click': '',
    'username_selector': "//input[@id='mobile']",
    'password_selector': "//input[@id='password']",
    'username': '13798495474',
    'password': 'minmin520',
    'submit_selector': "//input[@id='login']",
}

if __name__ == '__main__':
    login(confi)
