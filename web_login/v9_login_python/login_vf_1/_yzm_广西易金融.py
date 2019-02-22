import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '广西易金融',
    'save_path': ['D:\\火车采集器V9\\Data\\Cookie\\1840.txt'],
    'headless': False,
    'login_url': 'https://www.yjrzx.com/gxyjr/web/security/auth/signin',
    'vf_element_selector': "//img[@id='captcha-img']",
    'vf_text_element_elector': "//input[@id='captcha-code']",
    'username_element_selector': "//input[@id='loginName']",
    'username': 'minmin520',
    'spical_click': "//div[contains(@class,'login-list')]//div[2]//div[1]",
    'password_element_selector': "//input[@id='password']",
    'password': 'minmin520',
    'submit_selector': "//button[@id='btn-login']"
}


if __name__ == '__main__':
    web_vf_login(configuration)
