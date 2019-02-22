import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '小平贷',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\548.txt',
                  'E:\\4区火车头20160326\\Data\\Cookie\\1075.txt'],
    'headless': False,
    'login_url': 'https://www.xiaopingdai.com/user/login.html',
    'vf_element_selector': '//*[@id="login1"]/div/div[5]/img',
    'vf_text_element_elector': '//*[@id="validCode"]',
    'username_element_selector': '//*[@id="username"]',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login1"]/div/div[7]/input[1]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
