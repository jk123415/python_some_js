import sys
sys.path.append("..")
from no_vf_login import login

confi = {
    'name': '天一金融',
    'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1085.txt'],
    'url': 'http://www.tianyi77.com/loginAndRegiste/login.html',
    'headless': False,
    'bf_username_click': '/html/body/div/form/div/div[1]/label/i',
    'bf_password_click': '',
    'username_selector': '//*[@id="mobile"]',
    'password_selector': '//*[@id="password"]',
    'username': '13798495474',
    'password': 'minmin520',
    'submit_selector': '//*[@id="login"]',
}

if __name__ == '__main__':
    login(confi)
