#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-09 14:56:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.parse
import re
import time
path = r'C:\Users\Administrator\Desktop\spider\uilencode_href'
with open(path, encoding='utf-8', errors='ignore') as f:
    x = f.readlines()

# 工商信用


def gsxy(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            d = urllib.parse.quote(a)
            code = 'https://wx.szcredit.org.cn/weixin/Ajax/AjaxHandler.ashx?action=getSearchList&keyword='
            href = code + d + '\n'
            print(href)
            f.writelines(href)
    f.close()

# 天眼查


def _time(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            d = timestamp_to_date(a)
            code = 'https://www.tianyancha.com/search?key='
            href = d + '\n'
            print(href)
            f.writelines(href)
    f.close()

# 企查查


def qcc(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            d = urllib.parse.quote(a)
            code = 'https://www.qichacha.com/search?key='
            href = code + d + '\n'
            print(href)
            f.writelines(href)
    f.close()


def qxb(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            d = urllib.parse.quote(a)
            code = 'http://www.qixin.com/search?key='
            href = code + d + '&page=1' + '\n'
            print(href)
            f.writelines(href)
    f.close()

# 百度招聘


def bdzp(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            d = urllib.parse.quote(a)
            code = 'http://zhaopin.baidu.com/quanzhi?query='
            href = code + d + '\n'
            print(href)
            f.writelines(href)


def _51wd(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            d = urllib.parse.quote(a)
            code = 'http://www.51wangdai.com/search?key='
            href = code + d + '\n'
            print(href)
            f.writelines(href)


def date_to_timestamp(date, format_string="%Y-%m-%d"):
    time_array = time.strptime(date, format_string)
    time_stamp = int(time.mktime(time_array))
    return time_stamp


def _time_(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            d = urllib.parse.quote(a)
            code = 'https://www.szcredit.org.cn/SZXYMBWSercives/WeiXinCXService.asmx/GetList?sNameKey={}&DeptName=&EntType=&IndName=&DataTime=&idcode=ABcdef123321&secret=www.szcredit.org.cn'
            href = code.format(a) + '\n'
            print(href)
            f.writelines(href)

def glqy(x):
    f = open(path, 'w')
    if x:
        for i in x:
            a = i.strip()
            if a:
                d = urllib.parse.quote(a)
                code = 'https://www.qichacha.com/search?key='
                href = code + d + '\n'
                print(href)
                f.writelines(href)
    f.close()

_time_(x)