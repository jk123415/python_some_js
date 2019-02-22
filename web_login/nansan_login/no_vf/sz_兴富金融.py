import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '兴富金融',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1080.txt'],
    'url': 'http://www.huarunxf.cn/login.html',
    'headless': False,
    'bf_username_click': '//*[@id="j_username_placeholder"]',
    'bf_password_click': '',
    'username_selector': '//*[@id="j_username"]',
    'password_selector': '//*[@id="j_pass"]',
    'username': '15816057558',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginbut"]',
}

if __name__ == '__main__':
    login(confi)
