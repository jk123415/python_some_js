import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '贺邦投资',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1638.txt'],
    'headless': False,
    'login_url': 'http://www.hebangjiedai.com/p2pweb/enter.html',
    'vf_element_selector': "//img[@id='imgv']",
    'vf_text_element_elector': "//input[@id='validatecode']",
    'username_element_selector': "//input[@id='userid']",
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': "//input[@id='txtkey']",
    'password': 'minmin520',
    'submit_selector': "//input[@id='sendreg']"
}


if __name__ == '__main__':
    web_vf_login(configuration)
