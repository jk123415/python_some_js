import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '小树时代',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\302.txt',
                     "F:\\清莹\\火车采集器V8\\Data\\Cookie\\997.txt",
                     "F:\\清莹\\火车采集器V8\\Data\\Cookie\\301.txt",
                     "D:\\火车采集器V9\\Data\\Cookie\\1700.txt"],
    'url': 'https://www.xiaoshushidai.cn/user-invest_login',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="login-email-address"]',
    'password_selector': '//*[@id="login-password"]',
    'username': '15982657662',
    'password': 'MINmin520',
    'submit_selector': '//*[@id="user-login-submit"]',
}

if __name__ == '__main__':
    login(confi)
