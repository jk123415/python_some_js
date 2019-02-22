import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '前沿财富',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1080.txt'],
    'url': 'https://qycfu.com/visitor/to-login',
    'headless': False,
    'bf_username_click': '//*[@id="df_login"]',
    'bf_password_click': '',
    'username_selector': '//*[@id="username"]',
    'password_selector': '//*[@id="df_login"]/div/div[2]/dd/input',
    'username': '15816057558',
    'password': 'minmin520',
    'submit_selector': '//*[@id="df_login"]/div/div[3]/input',
}

if __name__ == '__main__':
    login(confi)
