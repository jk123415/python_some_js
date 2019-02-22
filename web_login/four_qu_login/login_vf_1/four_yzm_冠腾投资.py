import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '冠腾投资',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\92.txt'],
    'headless': False,
    'login_url': 'http://www.guantengdai.com/user/login',
    'vf_element_selector': '//*[@class="code_input"]/div/img',
    'vf_text_element_elector': '//*[@id="verify"]',
    'username_element_selector': '//*[@id="login-email-address"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="login-password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="user-login-submit"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
