import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '珊瑚树金融',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\1226.txt'],
    'headless': False,
    'login_url': 'https://www.shanhushu.com/login',
    'vf_element_selector': "//img[@id='captchar']",
    'vf_text_element_elector': "//input[@id='rancode']",
    'username_element_selector': "//input[@id='username']",
    'username': '15385381996',
    'spical_click': '',
    'password_element_selector': "//input[@id='password']",
    'password': 'minmin520',
    'submit_selector': "//button[@id='submitbtn']"
}


if __name__ == '__main__':
    web_vf_login(configuration)
#15385381996