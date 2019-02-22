import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '中盛金融e路贷',
    'cookies_path': ['E:\\4区火车头20160326\\Data\\Cookie\\1179.txt'],
    'url': 'http://www.tczsjr.com/loginAndRegiste/login.html',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': "//input[@id='mobile']",
    'password_selector': "//input[@id='password']",
    'username': '18078191783',
    'password': 'minmin520',
    'submit_selector': "//input[@id='login']",
}

if __name__ == '__main__':
    login(confi)
