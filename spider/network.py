#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-29 11:28:14
# @Author  : leopython (hailson@sina.com)
# @Link    : http://www.cnblogs.com/leopython/
# @Version : $Id$

import requests


def form_data(stri):
    if stri == '':
        return {}
    elif isinstance(stri, str):
        a = stri.split('&')
        data = {}
        for i in a:
            lst = i.split('=')
            data[lst[0]] = lst[1]
        return data
    elif isinstance(stri, dict):
        return stri
    else:
        pass


def header(stri):
    if stri == '':
        return dict()
    elif isinstance(stri, str):
        a = stri.split('\n')
        data = {}
        for i in a:
            lst = i.split(": ")
            data[lst[0]] = lst[1]
        return data
    else:
        pass

# lst = ['get','uri',{headers},{data}]


def request_uri(lst, headers):
    if lst[0] == 'get':
        uri_lst = []
        for i in range(lst[1][0], lst[1][1]):
            uri = lst[2].format(vari=i)
            uri_lst.append(uri)
        for uri in uri_lst:
            if headers == {}:
                r = requests.get(uri)
            else:
                r = requests.get(uri, headers=headers)
