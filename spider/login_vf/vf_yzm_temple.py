from selenium import webdriver
from PIL import Image
import tkinter
import os
import time
import random
from vf_gui import yzm


def cookies_handle(cookies):
    cookies_str = ''
    if cookies:
        for i in cookies:
            item = i['name'] + '=' + i['value'] + ';'
            cookies_str += item
    return cookies_str


def web_vf_login(configuration):
    options = webdriver.ChromeOptions()
    if configuration['headless']:
        options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(5)
    driver.get(configuration['login_url'])
    driver.set_window_size(1366, 768)
    if configuration.get('bf_click'):
        driver.find_element_by_xpath(configuration['bf_click']).click()
    time.sleep(1)
    name = str(random.random())
    rand_name = "a{}.png".format(name)
    driver.save_screenshot(rand_name)
    element = driver.find_element_by_xpath(
        configuration['vf_element_selector'])
    # print(element.location)                # 打印元素坐标
    # print(element.size)                    # 打印元素大小
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']
    try:
        im = Image.open(rand_name)
        im = im.crop((left, top, right, bottom))
        im.save(rand_name)
        filename = rand_name
        yzm_string = yzm(configuration['name'], filename)
        os.remove(rand_name)
        if configuration['spical_click']:
            driver.find_element_by_xpath(configuration['spical_click']).click()
        username = driver.find_element_by_xpath(
            configuration['username_element_selector'])
        username.send_keys(configuration['username'])
        if configuration['spical_click']:
            driver.find_element_by_xpath(configuration['spical_click']).click()
        password = driver.find_element_by_xpath(
            configuration['password_element_selector'])
        password.send_keys(configuration['password'])
        yzm_ele = driver.find_element_by_xpath(
            configuration['vf_text_element_elector'])
        yzm_ele.send_keys(yzm_string)
        submit = driver.find_element_by_xpath(configuration['submit_selector'])
        submit.click()
        time.sleep(5)
        cookies_list = driver.get_cookies()
    except Exception as e:
        try:
            os.remove(rand_name)
        except Exception:
            pass
        print(configuration['name'], '程序异常：', e)
        cookies_list = ""
    finally:
        driver.quit()
    cookies = cookies_handle(cookies_list)
    for path in configuration['save_path']:
        with open(path, 'w') as f:
            f.write(cookies)
    print(configuration['name'], 'cookie录入完成')


if __name__ == '__main__':
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
    web_vf_login(configuration)
