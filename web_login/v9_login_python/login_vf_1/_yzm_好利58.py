import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '好利58',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1804.txt', 'D:\\火车采集器V9\\Data\\Cookie\\1819.txt'],
    'headless': False,
    'login_url': 'https://www.haoli58.com/user/login',
    'vf_element_selector': '//*[@id="mobileCode-li"]/img',
    'vf_text_element_elector': '//*[@id="mobileCode-li"]/div/input',
    'username_element_selector': '//*[@id="mobile-li"]/div/input',
    'username': 'minmin520',
    'spical_click': '',
    'password_element_selector': '//*[@id="ng-app"]/div[2]/div/div[2]/div/div[2]/form/ul/li[2]/div/input',
    'password': 'minmin520',
    'submit_selector': '//*[@id="ng-app"]/div[2]/div/div[2]/div/div[2]/form/ul/li[5]/input[2]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
