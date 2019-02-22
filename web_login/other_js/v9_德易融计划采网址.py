import re
import requests
import json

target_url = 'https://www.derongtx.com/robot'
post_ = {"png": 1, "wait": 0.5, "load_args": {}, "http_method": "GET", "save_args": [], "html": 1, "images": 1, "resource_timeout": 0, "timeout": 90,
         "lua_source": "function main(splash, args)\r\n  assert(splash:go(args.url))\r\n  assert(splash:wait(0.5))\r\n  return {\r\n    html = splash:html(),\r\n    --png = splash:png(),\r\n    --har = splash:har(),\r\n  }\r\nend", "har": 1, "viewport": "1024x768", "response_body": False, "render_all": False,
         "url": target_url, "html5_media": False}

post_1 = {"png": 1, "wait": 0.5, "load_args": {}, "http_method": "GET", "save_args": [], "html": 1, "images": 1, "resource_timeout": 0, "timeout": 90,
          "lua_source": "function main(splash, args)\r\n  assert(splash:go(args.url))\r\n  assert(splash:wait(0.5))\r\n  local element = splash:select('li.addclass_li_3'):mouse_click{}\r\n  assert(splash:wait(2))\r\n  return {\r\n    html = splash:html(),\r\n  }\r\nend", "har": 1, "viewport": "1024x768", "response_body": False, "render_all": False,
          "url": target_url, "html5_media": False}

post_2 = {"png": 1, "wait": 0.5, "load_args": {}, "http_method": "GET", "save_args": [], "html": 1, "images": 1, "resource_timeout": 0, "timeout": 90,
          "lua_source": "function main(splash, args)\r\n  assert(splash:go(args.url))\r\n  assert(splash:wait(0.5))\r\n  local element = splash:select('.addclass_li_12 div'):mouse_click{}\r\n  assert(splash:wait(2))\r\n  return {\r\n    html = splash:html(),\r\n  }\r\nend", "har": 1, "viewport": "1024x768", "response_body": False, "render_all": False,
          "url": target_url, "html5_media": False}


def test(target_url, post_):
    requests_url = 'http://192.168.99.100:8050/execute'
    response = requests.post(requests_url, json=post_)
    content = response.text
    response_json = json.loads(content)
    html = response_json['html']
    pattern_href = '<font id="font_(.*?)">'
    return re.findall(pattern_href, html)


test_ = test(target_url, post_)
test_1 = test(target_url, post_1)
test_2 = test(target_url, post_2)
result = test_ + test_1 + test_2

path = 'C:\\Users\\Administrator\\Desktop\\脚本文档\\post\\德易融post.txt'

if result:
    with open(path, 'w') as f:
        for i in result:
            href_pattern = 'https://www.derongtx.com/ajax/getRobotLoans?page=1&size=20&robotId={}&_='
            href = href_pattern.format(i) + '\n'
            print(href)
            f.writelines(href)
