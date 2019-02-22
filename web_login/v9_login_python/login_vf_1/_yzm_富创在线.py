import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '富创在线',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1824.txt'],
    'headless': False,
    'login_url': 'https://www.futron.cn/?user&q=login',
    'vf_element_selector': '//*[@id="valicode"]',
    'vf_text_element_elector': '//*[@id="vericode"]',
    'username_element_selector': '//*[@id="username"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="log_sub"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
