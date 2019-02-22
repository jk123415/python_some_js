import sys
sys.path.append("..")
from vf_yzm_temple import web_vf_login

configuration = {
    'name': '影贷宝儿',
    'save_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1091.txt'],
    'headless': True,
    'login_url': 'http://www.yingdaibaoer.com/Index/User/login.html',
    'vf_element_selector': '//*[@id="vcode"]/span[1]/img',
    'vf_text_element_elector': '//*[@id="valicode"]',
    'username_element_selector': '//*[@id="username"]',
    'username': 'minmin520688',
    'spical_click': '',
    'password_element_selector': '//*[@id="password"]',
    'password': 'minmin520',
    'submit_selector': '//*[@id="loginSubBtn"]'
}


if __name__ == '__main__':
    web_vf_login(configuration)
