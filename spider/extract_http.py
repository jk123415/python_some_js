#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 16:21:33
# @Author  : leopython (hailson@sina.com)
# @Link    : http://www.cnblogs.com/leopython/
# @Version : $Id$

import os
import pprint
import re
import json
import jsonpath
import requests

variables = [{'uri': 'https://www.ztltw.com/rs/financing/queryInvestList',
              'cookies': '',
              'headers': '''Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 178
Content-Type: application/json; charset=UTF-8
Cookie: QVAxODA2MjcwMDAwMDAy=RkQxODA2MjcwMDAwMDAy; QVAxODA2MjcwMDAwMDAx=RkQxODA2MjcwMDAwMDAx; QVAxODA2MjYwMDAwMDA4=RkQxODA2MjYwMDAwMDA4; QVAxODA2MjUwMDAwMDAx=RkQxODA2MjUwMDAwMDAx; _TOKEN=MTAzMDc2OSxmMTk0NjcxOTBjOTk0YTliOTJmZTViYjE2NmQ4NWUwZiwxNTMwNzkzNjk5NzUz; Hm_lvt_f2af1c6d1b3c65686f4d05600226c2b2=1530774883,1530781537; Hm_lpvt_f2af1c6d1b3c65686f4d05600226c2b2=1530781581; _fmdata=D634gH0TahgsLmCNcQ1jajrTg7PKeNqtd4lVCzi2P%2BanCNI%2FbSA%2BxERqAlMXrYVcMa%2BczOKs4%2BFb9kx%2F45HserHrxVTgdQw9r%2FULFZDeIGk%3D; JSESSIONID=4D32A9CF1B1AD65872F8358DFACDE176
Host: www.ztltw.com
Origin: https://www.ztltw.com
Referer: https://www.ztltw.com/Financeproducts.html
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
X-Requested-With: XMLHttpRequest''',
              'post_data': '''{"greatTotalMoney":"","investPeriodGreat":"","investPeriodLess":"","isASC":false,"lessTotalMoney":"","limit":12,"orderBy":"create_time","start":%d,"type":null,"totalPageCount":47}''',
              # 变化部分用%d代替
              'range': (0, 600, 12),
              'orgin': 'https://www.ztltw.com',
              'file_adr': 'C:/Users/Administrator/Desktop/脚本文档/Test.txt',
              'rule': {'json': '$..orderId'},
              'switch': {'cookies_need': 1,  # 0 不需要cookie,1 自动cookie, 2,手动cookie
                         'headers_need': 0,  # 0 需要，1 不需要
                         'collect_data': 0,  # 0 提取post值，1提取网址
                         'uriii_change': 1,  # 0 uri变化，1 post变化
                         'post_pattern': 1,  # 0 form_data ; 1 payload
                         'collect_rule': 2,  # 0 bs提取，1正则表达式提取,2:json
                         }
              }, {'uri': '',
                  'cookies': '',
                  'headers': '''''',
                  'post_data': '''''',
                  # 变化部分用%d代替
                  'range': (1, 5, 1),
                  'orgin': '',
                  'file_adr': '',
                  'rule': '',
                  'switch': {'cookies_need': 0,  # 0 不需要cookie,1 自动cookie, 2,手动cookie
                             'headers_need': 0,  # 0 需要，1 不需要
                             'collect_data': 0,  # 0 提取post值，1提取网址
                             'uriii_change': 1,  # 0 uri变化，1 post变化
                             'post_pattern': 0,  # 0 form_data ; 1 payload
                             'collect_rule': 0,  # 0 bs提取，1正则表达式提取
                             }
                  }]


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


def payload_form(stri):
    reg = re.compile(r'{.*}')
    if re.search(reg, stri):
        return json.loads(stri)
    else:
        print(r"参数类型错误，必须类似 '{参数}'")


def exetract(variables):
    for vari in variables:
        if vari['uri'] == '':
            break
        switch = vari['switch']
        if switch['cookies_need'] == 0:  # 不需要cookie
            pass
        elif switch['cookies_need'] == 1:  # 自动获取cookie
            if vari['orgin'] == '':
                print('orgin 不得为空')
                input('请按回车键退出： ')
                break
            else:
                headers = header(vari['headers'])
                # r = requests.get(vari['orgin'])
                # header['cookie'] = ('; '.join(['='.join(item) for item in r.cookies.items()]))
                if switch['uriii_change'] == 0:  # 网址变化
                    pass
                else:  # postval change
                    post_value = ''
                    #num = 0
                    for par in range(vari['range'][0], vari['range'][1], vari['range'][2]):
                        if switch['post_pattern'] == 0:  # form_data
                            pass
                        else:  # payload
                            # print(vari['post_data'])
                            # print(par)
                            payload = vari['post_data'] % par
                            # print(payload)
                            js = json.dumps(payload_form(payload))
                            r = requests.post(
                                vari['uri'], data=payload, headers=headers)
                            if switch['collect_rule'] == 0:  # bs extract
                                pass
                            elif switch['collect_rule'] == 1:  # re extract
                                pass
                            else:  # json exetract
                                post_js = json.loads(r.text)
                                post_data = jsonpath.jsonpath(
                                    post_js, expr=vari['rule']['json'])
                                if not isinstance(post_data, list):
                                    break
                                post_value = post_value + \
                                    ('\n'.join(post_data))
                                # print(post_value)
                                pprint.pprint(post_data)
                            # print(r.text)
                            # break
                    # print(post_value)
                    with open(vari['file_adr'], 'w') as f:
                        f.write(post_value)
        else:  # 手动获取cookie
            pass


exetract(variables)

#input('请按回车键退出： ')
