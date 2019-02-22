import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '道普财富',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\78.txt'],
    'headless': False,
    'login_url': 'http://www.pudaocf.com/redirect.html?v=login',
    'vf_element_selector': "//img[@id='codeImage']",
    'vf_text_element_elector': "//input[@id='checkCode']",
    'username_element_selector': "//input[@id='loginInfo']",
    'username': 'minmin5202',
    'spical_click': '',
    'password_element_selector': "//input[@id='loginPwd']",
    'password': 'minmin520',
    'submit_selector': "//input[@value='登  录']"
}


if __name__ == '__main__':
    web_vf_login(configuration)
