#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-03 14:37:22
# @Author  : leopython (hailson@sina.com)
# @Link    : http://www.cnblogs.com/leopython/
# @Version : $Id$
import re
import pprint
import jsonpath
import requests
import json
import time
import sqlite3


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


def update_db(db_file, dic={}, conditions=''):
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    if conditions == '':
        columns = ', '.join(dic.keys())
        value = (', ?' * len(dic.keys())).strip(', ')
        s = 'select * from Content where 编号="%s"' % dic['编号']
        # print(s)
        db.execute(s)
        lst = db.fetchall()
        if lst == []:
            statement = 'insert into Content({}) values ({})'.format(
                columns, value)
            db.execute(statement, tuple(dic.values()))
        else:
            print(dic['标题'], ' 已经采集过')
            return
    else:
        for item in dic.items():
            # print(item)
            str = "UPDATE Content set {0}='{1}' where {2}".format(
                item[0], item[1], conditions)
            # print(str)
            db.execute(str)
    conn.commit()
    db.close()
    conn.close()
    print(dic['标题'], ' is done')


class Tag():

    def __init__(self, tag_name, tag_value, json):
        self.name = tag_name
        self.alias_name = tag_value['name']
        self.value = tag_value['value']
        if self.value != '':
            if '$' in self.value:
                if not (jsonpath.jsonpath(json, tag_value['value'])):
                    self.value = None
                else:
                    self.value = (
                        (jsonpath.jsonpath(json, tag_value['value']))[0])
        # print(tag_value['extend'].keys())
        # print(tag_value['extend'])
        if tag_value['extend'] == None:
            pass
        else:
            for extend_name, extend_rule in tag_value['extend'].items():
                # print(extend_name)
                if extend_name == 'calculate':
                    # print(extend_rule[0])
                    if extend_rule[0] == 'value':
                        if extend_rule[1] == '*':
                            self.value = str(float(self.value)
                                             * extend_rule[2])
                        elif extend_rule[1] == '+':
                            self.value = str(self.value) + extend_rule[2]
                    elif extend_rule[2] == 'value':
                        if extend_rule[1] == '-':
                            self.value = extend_rule[0] + '-' + self.value
                elif extend_name == 'timestamp':
                    time_stamp = str(self.value)
                    if time_stamp != 'None':
                        self.value = time.strftime(
                            '%Y-%m-%d %H:%M:%S', time.localtime(int(time_stamp[0:10])))
                elif extend_name == 'replace':
                    self.value = str(self.value).replace(
                        extend_rule[0], extend_rule[1])
                elif extend_name == 'loop_replace':
                    #self.value = list(self.value)
                    # print(type(self.value))
                    # print(self.value)
                    if self.value == None:
                        self.value = None
                    else:
                        investlist = ''
                        for ety in self.value:
                            stri = '{{username={0}|rate={1}|postmoney={2}|money={2}|postdate={3}|status=全部通过}}'.format(
                                ety[extend_rule[0]], ety[extend_rule[1]] * 100, ety[extend_rule[2]], ety[extend_rule[3]])
                            investlist += stri
                        self.value = investlist


class Entry():

    def __init__(self, json_data, variable):
        data = jsonpath.jsonpath(json_data, variable['base']['jsonpath_0'])
        for ety in data[0]:
            file_0 = {}
            file_1 = {}
            for tag_name, tag_value in variable['page_0']['tag'].items():
                tag = Tag(tag_name, tag_value, ety)
                dic = getattr(tag, '__dict__')
                file_0[dic['alias_name']] = str(dic['value'])
                file_1[dic['name']] = str(dic['value'])
                # print(dic)
            # pprint.pprint(ety)
            headers = header(variable['base']['headers'])
            replace = (jsonpath.jsonpath(
                ety, variable['page_1']['payload'][0]))[0]
            payload_1 = variable['page_1']['payload'][1] % replace
            re_1 = requests.post(variable['page_1'][
                                 'uri'], data=payload_1, headers=headers)
            js_1 = json.loads(re_1.text)
            for tag_name, tag_value in variable['page_1']['tag'].items():
                tag = Tag(tag_name, tag_value, js_1)
                dic = getattr(tag, '__dict__')
                file_0[dic['alias_name']] = str(dic['value'])
                file_1[dic['name']] = str(dic['value'])
                # print(getattr(tag,'__dict__'))
            # pprint.pprint(js)
            payload_2 = variable['page_2']['payload'][1] % replace
            re_2 = requests.post(variable['page_2'][
                                 'uri'], data=payload_2, headers=headers)
            js_2 = json.loads(re_2.text)
            # pprint.pprint(js_2)
            for tag_name, tag_value in variable['page_2']['tag'].items():
                tag = Tag(tag_name, tag_value, js_2)
                dic = getattr(tag, '__dict__')
                file_0[dic['alias_name']] = str(dic['value'])
                file_1[dic['name']] = str(dic['value'])
                # print(getattr(tag,'__dict__'))
            # pprint.pprint(js_2)
            # print(file_1,file_0)
            if file_0['时间'] != 'None':
                file_0['已采'] = 1
                update_db(variable['base']['db_file'], file_0)
            else:
                print(file_0['标题']	, '完成度不符合要求')
            # break


class Spider():

    def __init__(self):
        self.variable = ''

    def spider(self):
        page_0 = self.variable['page_0']
        headers = header(self.variable['base']['headers'])
        for num in range(page_0['payload'][0][0], page_0['payload'][0][1], page_0['payload'][0][2]):
            payload = page_0['payload'][1] % num
            r = requests.post(page_0['uri'], data=payload, headers=headers)
            # print(r.text)
            re_body = json.loads(r.text)
            Entry(re_body, self.variable)
            # break
spider = Spider()
spider.variable = { 'base': {'headers': '''Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 2
Content-Type: application/json; charset=UTF-8
Cookie: tokenId=MhCSxZHt3sCe7zY5wCaxcRfejW2EhiZf; JSESSIONID=22FCAAC900F3CE5C1F277F7BAB5BB4DA; QVAxODA3MzEwMDAwMDAy=RkQxODA3MzEwMDAwMDAy; QVAxODA3MzEwMDAwMDAz=RkQxODA3MzEwMDAwMDAz; QVAxODA3MzEwMDAwMDAx=RkQxODA3MzEwMDAwMDAx; QVAxODA3MzEwMDAwMDA0=RkQxODA3MzEwMDAwMDA0; Hm_lvt_f2af1c6d1b3c65686f4d05600226c2b2=1535452342,1535503428; _TOKEN=MTAzMDgzOSxlNTZmY2ZjMzM3Y2U0NGRkOTY4ZGQwYWExY2M4ZWM0NSwxNTM1NTIxNDYyMTg0; Hm_lpvt_f2af1c6d1b3c65686f4d05600226c2b2=1535503457; _fmdata=D634gH0TahgsLmCNcQ1jajrTg7PKeNqtd4lVCzi2P%2BanCNI%2FbSA%2BxERqAlMXrYVcDN8F%2BDIjONLK0Ap3sJCbSY2uuxak%2FqbV7emZBBCDdcE%3D
Host: www.ztltw.com
Origin: https://www.ztltw.com
Pragma: no-cache
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
X-Requested-With: XMLHttpRequest''',
                             'db_file': 'D:/火车采集器V9/Data/1742/SpiderResult.db3',
                             'jsonpath_0': '$..data',
                             'jsonpath_1': ''},
                    'page_0': {'uri': 'https://www.ztltw.com/rs/financing/queryInvestList',
                               'payload': ((0, 600, 12), '{"greatTotalMoney":"","investPeriodGreat":"","investPeriodLess":"","isASC":false,"lessTotalMoney":"","limit":12,"orderBy":"create_time","start":%d,"type":null,"totalPageCount":48}'),
                               'tag': {'title': {'name': '标题', 'value': '$.subjectName', 'extend': None},
                                       'borrowid': {'name': '编号', 'value': '$.orderId', 'extend': {'calculate': ('利投网', '-', 'value')}},
                                       'siteid': {'name': '网站编号', 'value': '7167', 'extend': None},
                                       'daystr': {'name': '借款期限', 'value': '$.investPeriod', 'extend': {'calculate': ('value', '+', '天')}},
                                       'money': {'name': '借款金额', 'value': '$.totalMoney', 'extend': None},
                                       'rate': {'name': '年利率', 'value': '$.baseRate', 'extend': {'calculate': ('value', '*', 100), }}, }},
                    'page_1': {'uri': 'https://www.ztltw.com/rs/financing/queryDetail',
                               'payload': ('$.orderId', '''{"orderId":"%s"}'''),
                               'tag': {'senddate': {'name': '发标时间', 'value': '$..startTime', 'extend': {'timestamp': (r'%Y%m%d%H%M%S', 10)}},
                                       'lastpostdate': {'name': '时间', 'value': '$..successTime', 'extend': {'timestamp': (r'%Y%m%d%H%M%S', 10)}},
                                       'username': {'name': '作者', 'value': '$..companyName', 'extend': None},
                                       'borrow_use': {'name': '借款用途', 'value': '$..loanUse', 'extend': None},
                                       'repayment_type': {'name': '还款方式', 'value': '$..payType', 'extend': {'replace': ('2', '4')}}}},
                    'page_2': {'uri': 'https://www.ztltw.com/rs/investOrder/queryInvenstorderList',
                               'payload': ('$.orderId', '{"limit":10,"start":0,"orderId":"%s","isAsc":false,"orderStatusList":[2,3,5]}'),
                               'tag': {'postdata': {'name': '回复内容', 'value': '$..data', 'extend': {'loop_replace': ('phoneNumber', 'lendRate', 'investMoney', 'investPeriod')}},
                                       'posttype': {'name': '回复类型', 'value': '1', 'extend': None},
                                       'borrow_url': {'name': '网址', 'value': 'https://www.ztltw.com/Financeproducts.html', 'extend': None}}}
                    }

spider.spider()
