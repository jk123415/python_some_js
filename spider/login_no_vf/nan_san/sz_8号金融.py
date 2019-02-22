import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '8号金融',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1081.txt'],
    'url': 'https://www.bahaojinrong.com/user/zhanghugaikuang',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="username"]',
    'password_selector': '//*[@id="password"]',
    'username': '15816057558',
    'password': 'minmin520',
    'submit_selector': '//*[@id="butt"]',
}

if __name__ == '__main__':
    login(confi)
