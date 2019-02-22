import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '金钥匙网贷',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1816.txt'],
    'headless': False,
    'login_url': 'https://www.jysp2p.com/loginIn.do?j=/account/memberfunds/index.do',
    'vf_element_selector': '//*[@id="imageId"]',
    'vf_text_element_elector': '//*[@id="codeYzm"]',
    'username_element_selector': '//*[@id="userName"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="passWord"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="submit"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
