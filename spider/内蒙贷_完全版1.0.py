#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-10 11:14:08
# @Author  : leopython (hailson@sina.com)
# @Link    : http://www.cnblogs.com/leopython/
# @Version : $Id$

import os
import requests
import pprint
import re
import sqlite3
from bs4 import BeautifulSoup
import lxml.html
import jsonpath

# 处理头消息


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
# 初始化数据库生成Content表


def initialize_db(db_file):
    post = {'title': "标题",
            'borrowid': "编号",
            'siteid': '网站编号',
            'lastpostdate': '时间',
            'daystr': '借款期限',
            'typeimg': '类型图片',
            'posttype': '回复类型',
            'postdata': '回复内容',
            'money': '借款金额',
            'rate': '年利率',
            'senddate': '发标时间',
            'username': '作者',
            'jiangli': '投标奖励',
            'jianglimoney': '奖励金额',
            'ratetype': '利率类型',
            'repayment_type': '还款方式',
            'borrow_url': '网址',
            'sex': '性别',
            'age': '年龄',
            'industry': '所属行业',
            'df': '所在地',
            'organization': '发布机构',
            'borrow_use': '借款用途',
            'borrower_type': '借款类别',
            'borrow_info': '借款详情', }
    print('''start initialize database: ''', db_file)
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    db.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_name = db.fetchall()
    if ('Content',) not in table_name:
        print('create table: Content in ', db_file)
        s = post.values()
        v = ''
        for i in s:
            c = ', ' + i + ' TEXT'
            v += c
        db.execute(
            '''CREATE TABLE Content(ID INTEGER PRIMARY KEY AUTOINCREMENT,已采 TINYINT(1),已发 TINYINT(1){})'''.format(v))
    else:
        print('already exist table: Content in ', db_file)
    conn.commit()
    conn.close()
# 更新数据库Content表列名，根据传入的lst


def update_db_field(db_file, lst=[]):
    print('start update table Content fields')
    # 链接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    db = conn.cursor()
    # 查询Content信息
    db.execute('''PRAGMA table_info([Content])''')
    # 获取查询结果
    colculmns = db.fetchall()
    # print(colculmns)
    # 生成空列表lt
    lt = []
    # 对查询结果进行迭代，生成lt 列名数据
    for col in colculmns:
        lt.append(col[1])
    # 对传入数据lst进行迭代
    for val in lst:
        # 判断lst中的字段是否在表content中存在
        if val not in lt:
            # 如果不存在，生成字段
            sta = '''ALTER TABLE Content ADD {} TEXT'''.format(val)
            # print(sta)
            db.execute(sta)
            print(val, ' is yes')
        else:
            # 如果存在则，返回yes
            # print('yes')
            pass
    print('Table Content fields already update')
    conn.commit()
    conn.close()
# 根据传入的字典更新数据库Content表信息


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
# 发布数据方法


def publish34(db_file):
    post = {'title': "标题",
            'borrowid': "编号",
            'siteid': '网站编号',
            'lastpostdate': '时间',
            'daystr': '借款期限',
            'typeimg': '类型图片',
            'posttype': '回复类型',
            'postdata': '回复内容',
            'money': '借款金额',
            'rate': '年利率',
            'senddate': '发标时间',
            'username': '作者',
            'jiangli': '投标奖励',
            'jianglimoney': '奖励金额',
            'ratetype': '利率类型',
            'repayment_type': '还款方式',
            'borrow_url': '网址',
            'sex': '性别',
            'age': '年龄',
            'industry': '所属行业',
            'df': '所在地',
            'organization': '发布机构',
            'borrow_use': '借款用途',
            'borrower_type': '借款类别',
            'borrow_info': '借款详情', }
    reg = re.compile('ok')
    post_uri = 'http://101.201.75.34/curl/insert.php'
    colculmus = ','.join(post.values())
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    db.execute('''SELECT {} FROM Content WHERE 已采=1 AND 已发=0'''.format(colculmus,))
    # print(db.fetchall())
    lst = db.fetchall()
    if lst == []:
        print('Need post data is 0')
        conn.close()
        return
    else:
        for postval in lst:
            publish_data = dict(zip(post.keys(), postval))
            # print(publish_data)
            rr = requests.post(post_uri, data=publish_data)
            if re.search(reg, rr.text):
                print(publish_data['title'], ' issued successfull')
                db.execute('''UPDATE Content SET 已发=1 WHERE 编号="{}"'''.format(
                    publish_data['borrowid']))
            else:
                print(publish_data['title'], ' issued failed')
                db.execute('''UPDATE Content SET 已发=2 WHERE 编号="{}"'''.format(
                    publish_data['borrowid']))
    conn.commit()
    conn.close()


# 标签类
class Tag():

    def __init__(self, name, value, entry, *body):
        self.name = name
        self.alias = value['name']
        self.value = value['value']
        if value['extend'] != {}:
            # print(value['extend'])
            for extend_name, extend_value in value['extend'].items():
                if extend_name == 'xpath' and extend_value[0] == 'text_content()':
                    html = lxml.html.fromstring(str(entry))
                    s = html.xpath(extend_value[1])
                    try:
                        f = s[0].text_content()
                        self.value = f.strip(' ')
                    except:
                        print(value['name'], ' 获取异常')
                elif extend_name == 'css':
                    # print(str(entry))
                    var = entry.select(extend_value[1])
                    if extend_value[0] == 'string':
                        # print(var)
                        self.value = str(var[0].string)
                    elif extend_value[0] == 'href':
                        self.value = str(var[0].get('href'))
                    elif extend_value[0] == 'remove_html_tag':
                        rr = re.compile('<.*?>')
                        # print(type(regx))
                        s = rr.subn('', str(var[0]))
                        self.value = s[0]
                        # print(s[0])
                elif extend_name == 'calculate':
                    if extend_value[0] == '+' and extend_value[2] == 'value':
                        self.value = extend_value[1] + self.value
                elif extend_name == 'substitute':
                    try:
                        rr = re.compile(extend_value[0])
                        s = re.search(rr, self.value)
                        self.value = s.group(extend_value[1])
                    except:
                        print(value['name'], ' 获取异常')
                    # print(s.group(1))
                elif extend_name == 'to_10000':
                    if re.search('万', self.value):
                        s = self.value.replace('万', '')
                        self.value = str(float(s) * 10000)
                        # print(s)
                elif extend_name == 'replace' and extend_value[0] == 'pay_method':
                    # print(extend_value)
                    try:
                        rr = re.compile('到期还本')
                        if re.search(rr, self.value):
                            self.value = 4
                    except:
                        print(value['name'], ' 获取异常')
                elif extend_name == 'loop_match':
                    # print(str(entry))
                    rr = re.compile(extend_value[0])
                    # print(extend_value[0])
                    #rr = re.compile(r'''<tr class="list_record tab1" >(?:.|\n)*?<td width="35%" style="text-align:left;">(.*?)</td>(?:.|\n)*?<td width="30%" style="">(.*?)</td>(?:.|\n)*?<td width="35%" style="text-align:right;">(.*?)</td>(?:.|\n)*?</tr>''')
                    # print(body[0])
                    n = rr.findall(body[0])
                    # print(n)
                    records = ''
                    for investrecord in n:
                        # print(investrecord)
                        # print(extend_value[1])
                        s = extend_value[1].format(t=investrecord)
                        records += s
                    # print(records)
                    self.value = records
                # elif extend_name == 'time_first':
                # elif extend_name == 'website_match':


class Entry():

    def __init__(self, entry, variable):
        #uri_1 = ''
        dic_0 = {}
        dic_1 = {}
        for tag_name, tag_value in variable['page_0']['tag'].items():
            tag = Tag(tag_name, tag_value, entry)
            ety = getattr(tag, '__dict__')
            # print(ety)
            dic_0[ety['alias']] = ety['value']
            dic_1[ety['name']] = ety['value']
        # print(dic_0)
        uri_1 = dic_0['网址']
        body = requests.get(uri_1).text
        content = BeautifulSoup(body, 'lxml')
        for tag_name, tag_value in variable['page_1']['tag'].items():
            tag = Tag(tag_name, tag_value, content, body)
            ety = getattr(tag, '__dict__')
            # print(ety)
            dic_0[ety['alias']] = ety['value']
            dic_1[ety['name']] = ety['value']
        # 编号从网址中采集
        # print(dic_0['编号']=='website_match')
        if dic_0['编号'] == 'website_match':
            # print(variable['page_1']['tag']['borrowid']['extend']['website_match'][0])
            rr = re.compile(variable['page_1']['tag']
                            ['borrowid']['extend']['website_match'][0])
            s = re.search(rr, dic_0['网址'])
            # print(s.group(1))
            # print(type(dic_0))
            dic_0['编号'] = variable['page_1']['tag']['borrowid']['extend']['website_match'][1] + \
                '-' + str(s.group(1))
        # 从回复内容中采时间
        if dic_0['时间'] == 'time_first':
            rr = re.compile(r'{.*?postdate=(.*?)\|status=全部通过}.*')
            s = re.search(rr, dic_0['回复内容'])
            dic_0['时间'] = s.group(1)
        # print(dic_0['完成度'])
        # sqlite3 入库===========================================================
        #
        #conn = sqlite3.connect(variable['base']['db_file'])
        if dic_0['完成度'] != '1':
            print(dic_0['标题'], '--未完成')
            dic_0['已采'] = 0
        elif 'noNone' in dic_0.values():
            dic_0['已采'] = 0
        else:
            dic_0['已采'] = 1
            dic_0['已发'] = 0
        # if dic_0['完成度'] ！='1':
        # print(dic_0['标题'],'未完成不采集')
        # pprint.pprint(dic_0)
        # 更新数据表Content数据
        if dic_0['已采'] == 1:
            update_db(variable['base']['db_file'], dic_0)


class Spyder():

    def __init__(self):
        self.variable = {}
    # 采集数据

    def spider(self):
        # 生成标签字段列表
        scope = {}
        scope['b'] = []
        scope['a'] = jsonpath.jsonpath(self.variable, expr='$..name')
        for i in scope['a']:
            scope['b'].append(i)
        # print(scope['b'])
        lts = scope['b']
        # 初始化数据库，生成Content表
        initialize_db(self.variable['base']['db_file'])
        # 根据标签更新数据库表Content字段
        update_db_field(self.variable['base']['db_file'], lts)
        for var in range(self.variable['page_0']['uri'][1][0], self.variable['page_0']['uri'][1][1]):
            # print(var)
            # print(self.variable['page_0']['uri'][0])
            url = self.variable['page_0']['uri'][0].format(var)
            # print(url)
            req_body = (requests.get(url)).text
            # print(req_body)
            soup = BeautifulSoup(req_body, 'lxml').find(
                'div', 'content3').contents
            soup.remove('\n')
            soup.remove(' ')
            #index = 0
            #s = (soup[0])
            # pprint.pprint(s)
            for ety in soup:
                # print(type(ety))
                # try:
                Entry(ety, self.variable)
                # except:
                # print('数据获取异常，联系技术人员')
        # 发布数据


spyder = Spyder()
spyder.variable = {
    'base': {'db_file': r'C:\Users\Administrator\Desktop\spider\db_file\Nmd.db3',  # 内蒙贷
             'headers': ''''''},
    'page_0': {'uri': ('https://www.nmgdai.com/Invest/investList/p/{}', (1, 7)),
               'tag': {'borrow_url': {'name': '网址', 'value': 'noNone', 'extend': {'css': ('href', '.block_r_txt1 > a'),
                                                                                  'calculate': ('+', 'https://www.nmgdai.com', 'value'), }},
                       'title': {'name': '标题', 'value': 'noNone', 'extend': {'css': ('string', '.block_r_txt1 > a'), }},
                       'progress': {'name': '完成度', 'value': 'noNone', 'extend': {'css': ('string', '.pertxt'), }}, }},
    'page_1': {'tag': {'money': {'name': '借款金额', 'value': 'noNone', 'extend': {'css': ('remove_html_tag', '.investDetail_span_money'),
                                                                               'substitute': (r'借款金额(.*?)元', 1),
                                                                               'to_10000': (), }},
                       'rate': {'name': '年利率', 'value': 'noNone', 'extend': {'xpath': ('text_content()', '/html/body/div[5]/div[1]/div[2]/span[2]/font/b'), }},
                       'daystr': {'name': '借款期限', 'value': 'noNone', 'extend': {'xpath': ('text_content()', '/html/body/div[5]/div[1]/div[2]/span[3]'),
                                                                                'substitute': (r'期限(.*)', 1)}},
                       'username': {'name': '作者', 'value': 'noNone', 'extend': {'xpath': ('text_content()', '/html/body/div[5]/div[1]/div[2]/span[4]'), }},
                       'senddate': {'name': '发标时间', 'value': 'noNone', 'extend': {'xpath': ('text_content()', '/html/body/div[5]/div[1]/div[3]/div[6]'),
                                                                                  'substitute': (r'上线时间：(.*)', 1)}},
                       'repayment_type': {'name': '还款方式', 'value': 'noNone', 'extend': {'xpath': ('text_content()', '/html/body/div[5]/div[1]/div[3]/div[2]'),
                                                                                        'substitute': (r'还款方式：(.*)', 1),
                                                                                        'replace': ('pay_method',)}},
                       'posttype': {'name': '回复类型', 'value': 1, 'extend': {}},
                       'postdata': {'name': '回复内容', 'value': 'noNone', 'extend': {'loop_match': (r'''<tr class="list_record tab1" >(?:.|\n)*?<td width="35%" style="text-align:left;">(.*?)</td>(?:.|\n)*?<td width="30%" style="">(.*?)</td>(?:.|\n)*?<td width="35%" style="text-align:right;">(.*?)</td>(?:.|\n)*?</tr>''', '{{username={t[1]}|rate=-1|postmoney={t[2]}|money={t[2]}|postdate={t[0]}|status=全部通过}}'), }},
                       'lastpostdate': {'name': '时间', 'value': 'time_first', 'extend': {'time_first': ()}},
                       'siteid': {'name': '网站编号', 'value': '5730', 'extend': {'time_first': ()}},
                       'borrowid': {'name': '编号', 'value': 'website_match', 'extend': {'website_match': (r'https://www.nmgdai.com/Invest/investDetail/borrow_id/(\w+)', '内蒙贷')}},
                       }},
    'page_2': {},
}

spyder.spider()
print(spyder.variable['base']['db_file'])
publish34(spyder.variable['base']['db_file'])
#input('请按回车键结束脚本： ')
