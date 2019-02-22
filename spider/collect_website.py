#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 10:48:18
# @Author  : leopython (hailson@sina.com)
# @Link    : http://www.cnblogs.com/leopython/
# @Version : $Id$

import os
import re
import pprint
import requests
import network
from bs4 import BeautifulSoup


vari = [{'orgin': 'http://hdhs.ygyd.com',
         '网址': 'http://hdhs.ygyd.com/organ/borrowList/{}',  # post 网址
         'post_from': '''data['deadlineS']: 1
data['limitS']: 1
data['statusS']: 1
data['repaymentS']: 1
param[repaymentS]: 1
param[statusS]: 1''',  # 发送的单表 页码用{}代替
         '页数': (1, 3),  # 起始页面和结束页码
         '请求头': '''Accept: text/html, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 136
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: JSESSIONID=FFCE7D8FDC6DA75CBCDE0A6211F3FB54
Host: hdhs.ygyd.com
Origin: http://hdhs.ygyd.com
Referer: http://hdhs.ygyd.com/organ/borrowIndex
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
X-Requested-With: XMLHttpRequest''',
         '保存地址': 'C:/Users/Administrator/Desktop/脚本文档/网址/邯山展宇.txt'
         },
        {'orgin': 'http://czygyd.com',
         '网址': 'http://czygyd.com/organ/borrowList/{}',  # post 网址  页码用{}代替
         'post_from': '''data['deadlineS']: 1
data['limitS']: 1
data['statusS']: 1
data['repaymentS']: 1
param[repaymentS]: 1
param[statusS]: 1''',  # 发送的单表
         '页数': (1, 2),  # 起始页面和结束页码      #重新贴cookie
         '请求头': '''Accept: text/html, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 136
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: JSESSIONID=626A196A0FF24CED5B86093FCC719998
Host: czygyd.com
Origin: http://czygyd.com
Referer: http://czygyd.com/organ/borrowIndex
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
X-Requested-With: XMLHttpRequest''',
         '保存地址': 'C:/Users/Administrator/Desktop/脚本文档/网址/阳光博发.txt'
         }, {'orgin': 'http://www.hhhtlyygyd.com',  # 必须包含http
             '网址': 'http://www.hhhtlyygyd.com/organ/borrowList/{}',  # post 网址，页码用{}代替
             'post_from': '''data['deadlineS']: 1
data['limitS']: 1
data['statusS']: 1
data['repaymentS']: 1
param[repaymentS]: 1
param[statusS]: 1''',  # 发送的单表
             '页数': (1, 2),  # 起始页面和结束页码-1
             '请求头': '''Accept: text/html, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 136
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: JSESSIONID=66E4D4A8DC260BD13D8698CB705EAE86
Host: www.hhhtlyygyd.com
Origin: http://www.hhhtlyygyd.com
Referer: http://www.hhhtlyygyd.com/organ/borrowIndex
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
X-Requested-With: XMLHttpRequest''',
             '保存地址': 'C:/Users/Administrator/Desktop/脚本文档/网址/呼和浩特利友.txt'
             }, {'orgin': '',  # 必须包含http
                 '网址': '',  # post 网址
                 'post_from': '''''',  # 发送的单表 页码用{}代替
                 '页数': (1, 3),  # 起始页面和结束页码
                 '请求头': '''''',
                 '保存地址': ''
                 }, {'orgin': '',  # 必须包含http
                     '网址': '',  # post 网址
                     'post_from': '''''',  # 发送的单表 页码用{}代替
                     '页数': (1, 3),  # 起始页面和结束页码
                     '请求头': '''''',
                     '保存地址': ''
                     }]

for vari in vari:
    if vari['网址'] == '':
        break
    r = requests.get(vari['orgin'])
    cookies = ('; '.join(['='.join(item) for item in r.cookies.items()]))
    postval = network.header(vari['post_from'])
    headers = network.header(vari['请求头'])
    headers['Cookie'] = cookies
    lst = []
    for i in range(vari['页数'][0], vari['页数'][1]):
        u = vari['网址'].format(i)
        r = requests.post(u, data=postval, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        links = soup.find_all('a')
        rr = re.compile(r'http')
        for link in links:
            lk = link.get('href')
            if re.search(rr, lk):
                if lk not in lst:
                    lst.append(lk)
                    print(lk, ' is done')
    with open(vari['保存地址'], "wt") as out_file:
        out_file.write('\n'.join(lst))
