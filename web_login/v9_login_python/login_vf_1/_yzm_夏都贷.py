import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '夏都贷',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1748.txt'],
    'headless': False,
    'login_url': 'http://www.xiadudai.com/user/loginUI.action',
    'vf_element_selector': '//*[@id="codeImage"]',
    'vf_text_element_elector': '//*[@id="verifyCode"]',
    'username_element_selector': '//*[@id="usrName"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginButton"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
