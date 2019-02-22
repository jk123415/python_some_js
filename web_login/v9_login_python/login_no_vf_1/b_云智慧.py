import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '云智慧',
    'cookies_path': ['D:\\火车采集器V9\\Data\\Cookie\\1811.txt'],
    'url': 'https://www.yunzhihuijr.com/user/login',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="IDtel"]',
    'password_selector': '//*[@id="IDpass"]',
    'username': '13266700657',
    'password': 'minmin520',
    'submit_selector': '/html/body/div[2]/div[2]/div/div[1]/a',
}

if __name__ == '__main__':
    login(confi)
