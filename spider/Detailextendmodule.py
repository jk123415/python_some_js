#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-13 10:47:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import sqlite3
import requests
import re
import pprint
from lxml import etree


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


def format_postval(exp, stri, result):
    a = re.findall(exp, stri)
    if a:
        b = result.format(a[0])
        lst = b.split('&')
        c = []
        for x in lst:
            y = x.split('=')
            c.append(y)
        return dict(c)
    else:
        print('associate_page_post_val handle error')


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


def paymethodreplace(string):
    if isinstance(string, str):
        a = '到期还本付息'
        b = '一次性'
        c = '等额本息'
        d = '每月付息'
        e = '一次付清'
        if re.search(a, string):
            return 3
        elif re.search(b, string):
            return 3
        elif re.search(c, string):
            return 2
        elif re.search(d, string):
            return 4
        elif re.search(e, string):
            return 3
        else:
            return 0
    else:
        print(string, "--object type is error")
        return 0


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
        string = re.subn(',', '', string)[0]
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
    db.execute(
        '''SELECT {} FROM Content WHERE 已采=1 AND 已发 is Null'''.format(colculmus,))
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


def xpathExtract(code, selector):
    lxmlpage = etree.HTML(code)
    e = lxmlpage.xpath(selector)
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
        return ''


def cssExtract(soup, selector):
    try:
        data = soup.select(selector)
        if data:
            a = ''
            for i in data:
                a += i.text
            return a
        else:
            return ''
    except NotImplementedError:
        print(tag_name,
              ' css selector is error, please change "nth-child" to "nth-of-type"')


def noNone(para):
    if not para:
        return 'error'
    else:
        return para


def htmlTagClear(para):
    if para:
        # extract para isn't none
        a = re.compile(r'[\s\r\n\t]')
        return a.subn('', para)[0]


def mustContain(para, value):
    b = re.compile(value)
    if b.match(para):
        return para
    else:
        print(para, "error--mustContain")
        return "error"


def noContain(para, value):
    b = re.compile(value)
    if b.match(para):
        print(para, "error--mustContain")
        return 'error'
    else:
        return para


def regex_clear(para, value):
    ss = re.subn(value, "", para)
    return ss[0]


def base_handle(para, value):
    try:
        ss = re.sub('参数', para, value)
    except TypeError:
        return ""
    return ss


def investRecords(para, value):
    if para:
        records = ''
        for i in para:
            try:
                records += value.format(t=i)
            except IndexError:
                print('tuple index out of range')
                return ''
        return records
    else:
        return None


def manually_extract_uri(response, expression, combinestr):
    uri = []
    body = response.text
    result = re.findall(expression, body)
    if result:
        for i in result:
            uri.append(combinestr.format(var_1=i))
    return uri


def get_method_link(uri, headers, info):
    try:
        body = requests.get(uri, headers=headers).text
    except:
        print('requests.get is error,please check uri',)
    lst = re.findall(info['extExp'], body)
    links = []
    if not lst:
        print('Extract links is 0')
    else:
        for i in lst:
            href = info['resultUri'].format(str(i))
            print(href)
            links.append(href)
    return links


def post_method_link(uri, headers):
    pass


def save_uri(db_file, links):
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    dup = 0
    if links:
        for link in links:
            a = 'select * from Content where 网址="%s"' % link
            db.execute(a)
            if db.fetchall():
                # The results of the query isn't []
                dup += 1
            else:
                # The results of the query is []
                db.execute('insert into Content (网址) values ("%s")' % link)
    print(',duplicated uri_num is', dup)
    conn.commit()
    db.close()
    conn.close()


def get_method_content(uri, headers):
    try:
        body = requests.get(uri, headers=headers)
    except:
        print('get_method_content is error:', uri)
    return body


def post_method_content(uri, postval, headers):
    try:
        body = requests.post(uri, data=postval, headers=headers)
    except:
        print('post_method_error:', postval)
    return body


def regex_extract_data(exp, string):
    try:
        f = re.findall(exp, string)
    except:
        f = ''
        print(exp, 'is error')
    return f


def get_target_uri(p):
    db_file = p['base']['db']
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    s = 'select 网址 from Content where 已采 is Null'
    db.execute(s)
    ls = db.fetchall()
    db.close()
    conn.close()
    if ls:
        return [x for x in ls for x in x]
    else:
        print('need extract href is 0')
        return None
