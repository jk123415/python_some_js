import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '中正易贷',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\296.txt'],
    'headless': False,
    'login_url': 'http://www.zhongzhengyidai.com/member/common/login.html',
    'vf_element_selector': "//img[@id='imVcode']",
    'vf_text_element_elector': "//input[@id='txtCode']",
    'username_element_selector': "//input[@id='txtUser']",
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': "//input[@id='txtPwd']",
    'password': 'minmin520',
    'submit_selector': "//a[@id='btnReg']"
}


if __name__ == '__main__':
    web_vf_login(configuration)
