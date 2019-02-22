import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '大信财富',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1099.txt'],
    'url': 'https://www.dasincapital.com/login.do',
    'headless': False,
    'bf_username_click': '//*[@id="p_username"]',
    'bf_password_click': '//*[@id="p_pwd"]',
    'username_selector': '//*[@id="CI_NM"]',
    'password_selector': '//*[@id="PWD"]',
    'username': 'minmin520',
    'password': 'minmin520188',
    'submit_selector': '//*[@id="J_login_btn"]',
}

if __name__ == '__main__':
    login(confi)
