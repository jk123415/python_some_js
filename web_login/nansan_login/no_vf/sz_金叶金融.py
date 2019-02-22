import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '金叶金融',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1066.txt',
                     'F:\\清莹\\火车采集器V8\\Data\\Cookie\\1067.txt'],
    'url': 'https://bank.jyjr168.com/loginWeb.jsp',
    'headless': True,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@id="loginName"]',
    'password_selector': '//*[@id="loginPwd"]',
    'username': '13421464186',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login_submit"]',
    'additional_cookie': []
}

if __name__ == '__main__':
    login(confi)
