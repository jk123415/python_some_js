import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '亚恒投资',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\46.txt'],
    'headless': False,
    'login_url': 'http://www.0311touzi.com/index.php?user&q=action/login',
    'vf_element_selector': "//img[@src='/plugins/index.php?q=imgcode']",
    'vf_text_element_elector': "//input[@placeholder='请输入验证码']",
    'username_element_selector': "//input[@id='keywords']",
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': "//input[@id='password']",
    'password': 'minmin520',
    'submit_selector': "//input[contains(@value,'录')]"
}


if __name__ == '__main__':
    web_vf_login(configuration)
