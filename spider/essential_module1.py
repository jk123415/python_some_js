#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-09 08:41:36
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import sqlite3
import re


def initialize_db(db_file):
    post = {'title': "标题", 'borrowid': "编号", 'siteid': '网站编号', 'lastpostdate': '时间', 'daystr': '借款期限', 'typeimg': '类型图片', 'posttype': '回复类型', 'postdata': '回复内容', 'money': '借款金额', 'rate': '年利率', 'senddate': '发标时间', 'username': '作者', 'jiangli': '投标奖励',
            'jianglimoney': '奖励金额', 'ratetype': '利率类型', 'repayment_type': '还款方式', 'borrow_url': '网址', 'sex': '性别', 'age': '年龄', 'industry': '所属行业', 'df': '所在地', 'organization': '发布机构', 'borrow_use': '借款用途', 'borrower_type': '借款类别', 'borrow_info': '借款详情', }
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


def format_headers(stri):
    if stri == '':
        return dict()
    elif isinstance(stri, str):
        a = stri.split('\n')
        data = {}
        for i in a:
            lst = i.split(": ")
            data[lst[0]] = lst[1]
        return data


def format_postval(stri):
    lst = stri.split('&')
    z = []
    for x in lst:
        y = x.split('=')
        z.append(y)
    return dict(z)


def update_db_field(db_file, lst):
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


def update_table_data(db, dic):
    data = []
    for key, values in dic.items():
        values = "'{}'".format(values)
        f = "{}={}".format(key, values)
        data.append(f)
    a = ', '.join(data)
    href = dic['网址']
    b = "UPDATE Content SET {a} WHERE 网址='{link}'".format(a=a, link=href)
    db.execute(b)
    print(dic['标题'], ' is done')


def update_db(db_file, dic, conditions=''):
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    if conditions:
        columns = ', '.join(dic.keys())
        value = (', ?' * len(dic.keys())).strip(', ')
        s = 'select * from Content where 编号="%s"' % dic['编号']
        # print(s)
        db.execute(s)
        lst = db.fetchall()
        if len(list) == 0:
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


def paymethodreplace(string):
    if isinstance(string, str):
        a = '到期还本'
        b = '一次性'
        c = '等额本息'
        if re.search(a, string):
            return 4
        elif re.search(b, string):
            return 3
        elif re.search(c, string):
            return 2
    else:
        print(string, "--object type is error")


def rataformat(string):
    if isinstance(string, str):
        a = '%'
        if re.search(a, string):
            return re.sub(a, "", string)
    else:
        print(string, "--object type is error")


def amountformat(string):
    if isinstance(string, str):
        a = '万元'
        b = '万'
        c = '元'
        if re.search(a, string):
            x = re.sub(a, "", string)
            return float(x) * 10000
        elif re.search(b, string):
            x = re.sub(b, "", string)
            return float(x) * 10000
        elif re.search(c, string):
            return re.sub(c, "", string)
    else:
        print(string, "--object type is error")


def publish_data_34(db_file):
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


def regexExtract(expression, sourcecode):
    a = re.subn(r'\\', r'\\\\', expression)
    b = re.findall(a, sourcecode)
    return b


def xpathExtract(lxmlpage, selector):
    a = lxmlpage.xpath(selector)
    if e:
        # xpath extract data isn't []
        try:
            f = ''
            for z in e:
                f += z.xpath('string(.)')
        except AttributeError:
            f = ''.join(e)
        return f
    else:
        # xpath extract data is []
        return None


def cssExtract(soup, selector):
    try:
        data = soup.select(selector)
        if data:
            a = ''
            for i in data:
                a += i.text
            return a
        else:
            return None
    except NotImplementedError:
        print(tag_name,
              ' css selector is error, please change "nth-child" to "nth-of-type"')


def dataFilter(data, dic={}):
    if dic:
        for name, value in dic.items():
            # extract data isn't none
            if name == 'htmlTagClear' and value:
                if data:
                    # extract data isn't none
                    a = re.compile(r'[\s\r\n\t]')
                    data = a.subn('', data)[0]
            if name == 'noNone' and value:
                if not data:
                    print(x, "error--noNone")
                    return True
            if name == 'mustContain' and value:
                b = re.compile(value)
                if not b.match(data):
                    print(x, "error--mustContain")
                    return True
            if name == 'paymethodreplace' and value:
                d = '万元'
                e = '万'
                f = '元'
                if re.search(d, data):
                    g = re.sub(d, "", data)
                    data = float(g) * 10000
                elif re.search(e, data):
                    g = re.sub(e, "", data)
                    data = float(g) * 10000
                elif re.search(f, data):
                    data = re.sub(f, "", data)
            if name == 'amountformat' and value:
                if isinstance(data, str):
                    a = '到期还本付息'
                    b = '一次性'
                    c = '等额本息'
                    d = '到期还本'
                    if re.search(a, data):
                        data = 3
                    elif re.search(b, data):
                        data = 3
                    elif re.search(c, data):
                        data = 2
                    elif re.search(d, data):
                        data = 3
                    else:
                        data = None


def manually_extract_uri(response, expression, combinestr):
    uri = []
    body = response.text
    result = re.findall(expression, body)
    if result:
        for i in result:
            uri.append(combinestr.format(var_1=i))
    return uri
