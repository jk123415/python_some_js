import sys
sys.path.append("..")
from no_vf_login import login


confi = {
    'name': '聚雪球',
    'cookies_path': ['D:\\火车采集器V9\\Data\\Cookie\\1727.txt'],
    'url': 'https://www.juxueqiu.com/index.php/login',
    'headless': False,
    'bf_username_click': '',
    'bf_password_click': '',
    'username_selector': '//*[@name="sjh"]',
    'password_selector': '//*[@name="mm"]',
    'username': '15982657662',
    'password': 'minmin520',
    'submit_selector': '//*[@id="reg_xyb"]',
}

if __name__ == '__main__':
    login(confi)
