import sys
sys.path.append("../..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '万贷金融',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\16617.txt'],
    'headless': True,
    'login_url': 'http://www.wandaijinrong.com/user/login',
    'vf_element_selector': '//*[@id="formv"]/div[4]/img',
    'vf_text_element_elector': '//*[@id="verifyCodeId"]',
    'username_element_selector': '//*[@id="user_username"]',
    'username': '15982657662',
    'spical_click': '',
    'password_element_selector': '//*[@id="formv"]/div[3]/input',
    'password': 'minmin520',
    'submit_selector': '//*[@id="btn_login"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
