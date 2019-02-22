import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '宜民贷',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\417.txt'],
    'headless': False,
    'login_url': 'http://www.yimindai.com/user/login.html',
    'vf_element_selector': "//img[@id='imgCode']",
    'vf_text_element_elector': "//input[@id='validcode']",
    'username_element_selector': "//input[@id='username']",
    'username': '18681466720',
    'spical_click': '',
    'password_element_selector': "//input[@id='password']",
    'password': 'minmin520',
    'submit_selector': "//a[@id='btn-login']"
}


if __name__ == '__main__':
    web_vf_login(configuration)
