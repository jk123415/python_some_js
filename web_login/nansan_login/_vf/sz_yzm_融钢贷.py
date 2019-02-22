import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '融钢贷',
    'save_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1075.txt'],
    'headless': False,
    'login_url': 'https://www.rongpd.com/loginPage',
    'vf_element_selector': '//*[@id="verify_img"]',
    'vf_text_element_elector': '//*[@id="form-validation-field-0"]',
    'username_element_selector': '//*[@id="username"]',
    'username': '13421464186',
    'spical_click': '',
    'password_element_selector': '//*[@id="pwd"]',
    'password': 'minmin520',
    'submit_selector': '/html/body/div[3]/div/div/ul[1]/li[5]/a'
}


if __name__ == '__main__':
    web_vf_login(configuration)
