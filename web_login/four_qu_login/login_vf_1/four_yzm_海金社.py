import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '海金社',
    'save_path': ['E:\\4区火车头20160326\\Data\\Cookie\\590.txt'],
    'headless': True,
    'login_url': 'https://www.haijinshe.com.cn/user/login.html',
    'vf_element_selector': '//*[@id="login"]/dl/dd[3]/img',
    'vf_text_element_elector': '//*[@id="login"]/dl/dd[3]/input',
    'username_element_selector': '//*[@id="username"]',
    'username': '13066900207',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login"]/dl/dd[6]/input'
}


if __name__ == '__main__':
    web_vf_login(configuration)
