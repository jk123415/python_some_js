import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '手贷网',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1809.txt'],
    'headless': True,
    'login_url': 'https://www.51sdw.com/login.html',
    'vf_element_selector': '//*[@id="imgLoginRand"]',
    'vf_text_element_elector': '//*[@id="r"]',
    'username_element_selector': '//*[@id="userName"]',
    'username': '13266700657',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginBox"]/div/div[4]/input[2]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
