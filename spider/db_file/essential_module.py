#!/usr/bin/env python

import requests
import sqlite3
import re


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
        db.execute('''CREATE TABLE Content(ID INTEGER PRIMARY KEY AUTOINCREMENT,已采 TINYINT(1),已发 TINYINT(1){})'''.format(v))
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


def update_db(db_file, dic, conditions=''):
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    if conditions == '':
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
    if list:
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



