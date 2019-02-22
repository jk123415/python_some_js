import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '葫芦时贷',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1730.txt'],
    'headless': False,
    'login_url': 'http://www.hulushidai.com/login',
    'vf_element_selector': '//*[@id="img"]',
    'vf_text_element_elector': '//*[@id="code"]',
    'username_element_selector': '//*[@id="name"]',
    'username': '15982657662',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'time_sleep': True,
    'submit_selector': '//*[@class="p_dl_btn p_op"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
