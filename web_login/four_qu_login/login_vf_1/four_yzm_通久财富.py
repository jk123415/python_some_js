import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '通久财富',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\1219.txt'],
    'headless': False,
    'login_url': 'http://www.tongjiucaifu.com/index.php/Member/Login/index.html',
    'vf_element_selector': '//*[@id="verify_img"]',
    'vf_text_element_elector': '//*[@id="Jverify"]',
    'username_element_selector': '//*[@id="login-email-address"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="login-password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="user-login-submit"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
