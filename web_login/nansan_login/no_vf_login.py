
from selenium import webdriver
import time


def cookies_handle(cookies):
    cookies_str = ''
    if cookies:
        for i in cookies:
            item = i['name'] + '=' + i['value'] + ';'
            cookies_str += item
    return cookies_str


def login(confi):
    url = confi['url']

    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    options.add_experimental_option('prefs', prefs)
    if confi['headless']:
        options.add_argument('--headless')
    chrome = webdriver.Chrome(chrome_options=options)
    try:
        chrome.get(url)
        chrome.set_window_size(1366, 768)
        # print('open page: ', url)
        time.sleep(2)
        if confi['bf_username_click']:
            chrome.find_element_by_xpath(confi['bf_username_click']).click()
        username = chrome.find_element_by_xpath(confi['username_selector'])
        username.send_keys(confi['username'])
        # print('enter username: 15982657662')
        if confi['bf_password_click']:
            chrome.find_element_by_xpath(confi['bf_password_click']).click()
        password = chrome.find_element_by_xpath(confi['password_selector'])
        password.send_keys(confi['password'])
        # print('enter password: minmin520')
        submit = chrome.find_element_by_xpath(confi['submit_selector'])
        submit.click()
        # print('submit data')
        time.sleep(3)
        if confi.get('haveAlert'):
            # print(123)
            alert = chrome.switch_to_alert()
            alert.accept()
        if confi.get('wait_time'):
            time.sleep(confi.get('wait_time'))
        if confi.get("additional"):
            for i in confi.get('additional'):
                exec(i)
        cookies_list = chrome.get_cookies()
        # time.sleep(20)
    except Exception as e:
        print(confi['name'], 'cookie采集异常: ', e)
        cookies_list = ''
    finally:
        chrome.quit()
    cookies = cookies_handle(cookies_list)
    for path in confi['cookies_path']:
        with open(path, "w") as f:
            f.write(cookies)
    print(confi['name'], 'cookie录入完成')


if __name__ == '__main__':
    confi = {
        'name': '兴富金融',
        'cookies_path': ['F:\\清莹\\火车采集器V8\\Data\\Cookie\\1080.txt'],
        'url': 'http://www.huarunxf.cn/login.html',
        'headless': False,
        'bf_username_click': '//*[@id="j_username_placeholder"]',
        'bf_password_click': '',
        'username_selector': '//*[@id="j_username"]',
        'password_selector': '//*[@id="j_pass"]',
        'username': '15816057558',
        'password': 'minmin520',
        'submit_selector': '//*[@id="loginbut"]',
    }
    login(confi)
