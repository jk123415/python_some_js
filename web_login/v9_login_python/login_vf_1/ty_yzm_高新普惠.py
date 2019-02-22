import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '高新普惠',
    'save_path': ('D:\\火车采集器V9\\Data\\Cookie\\1624.txt', ),
    'headless': False,
    'login_url': 'https://www.gaoxinzb.com/kasp/login.html',
    'vf_element_selector': '//*[@id="codeimg"]',
    'vf_text_element_elector': '//*[@id="loginform"]/ul/li[3]/input',
    'username_element_selector': '//*[@id="custid"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginform"]/ul/li[4]/input',
}


if __name__ == '__main__':
    web_vf_login(configuration)
