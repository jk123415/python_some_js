import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '宏信大众投',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1796.txt'],
    'headless': True,
    'login_url': 'https://www.zhijianjinrong.cn/',
    'bf_click': '//a[@class="login_a"]',
    'vf_element_selector': '//*[@id="randomimg"]',
    'vf_text_element_elector': '//*[@id="loginvalidcode"]',
    'username_element_selector': '//*[@id="username"]',
    'username': '15982657662',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="longinbtn"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
