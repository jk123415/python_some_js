import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '鸿坤金服',
    'save_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1051.txt'],
    'headless': True,
    'login_url': 'https://www.hongkunjinfu.com/login.do?method=tologin',
    'vf_element_selector': '//*[@id="loginform"]/div/div/div/div/ul/li[3]/cite[2]/img',
    'vf_text_element_elector': '//*[@id="yzm"]',
    'username_element_selector': '//*[@id="login"]',
    'username': '13798495474',
    'spical_click': '//*[@id="txt2"]',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="btn_sub"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
