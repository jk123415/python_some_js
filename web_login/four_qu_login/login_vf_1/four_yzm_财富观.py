import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '财富观',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\1224.txt'],
    'headless': True,
    'login_url': 'https://www.caifuguan.com/userLogin?userRole=01',
    'vf_element_selector': '//*[@id="checkImg"]',
    'vf_text_element_elector': '//*[@id="checkcode"]',
    'username_element_selector': '//*[@id="account"]',
    'username': '15278398569',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
