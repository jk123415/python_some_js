import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '众拓贷',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\608.txt'],
    'headless': False,
    'login_url': 'https://www.zhongtuo99.com/htmllogin.do?retUrl=indexlogin.do',
    'vf_element_selector': "//img[@id='loginCode']",
    'vf_text_element_elector': "//input[@id='checkCode']",
    'username_element_selector': "//input[@id='loginname']",
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': "//input[@id='password']",
    'password': 'minmin520',
    'submit_selector': "//span[@id='loginBtn']"
}


if __name__ == '__main__':
    web_vf_login(configuration)
