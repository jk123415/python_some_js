import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '芝麻贷',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\28.txt'],
    'headless': False,
    'login_url': 'https://www.zmdai.com/login',
    'vf_element_selector': '//*[@id="img"]',
    'vf_text_element_elector': '//*[@id="code"]',
    'username_element_selector': '//*[@id="name"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@class="p_zc_btn p_op"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
