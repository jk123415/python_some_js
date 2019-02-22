#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-25 21:40:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import sqlite3
import pprint
import pprint

# example (db_file,'*','id=0')
# return a list


def get_data_from_db(lst=[]):
    conn = sqlite3.connect(lst[0])
    db = conn.cursor()
    db.execute('PRAGMA table_info([Content])')
    arr = db.fetchall()
    arr_1 = []
    for i in arr:
        arr_1.append(i[1])
    if len(lst) == 2:
        statement = 'select * from Content where ' + lst[1]
    elif len(lst) == 3:
        statement = 'select ' + lst[1] + ' from Content where ' + lst[2]
    else:
        print('get_data_from_db() 参数错误')
    # print(statement)
    db.execute(statement)
    arr = db.fetchall()
    if len(lst) == 2:
        arr_2 = []
        for i in arr:
            l = dict(zip(arr_1, i))
            arr_2.append(l)
        return arr_2
    else:
        arr_2 = []
        for i in arr:
            arr_2.append(i[0])
        return tuple(arr_2)
    conn.close


def update_db(db_file, dic={}, conditions=''):
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    if conditions == '':
        columns = ', '.join(dic.keys())
        value = (', ?' * len(dic.keys())).strip(', ')
        s = 'select * from Content where 编号="%s"' % dic['编号']
        #print(s)
        db.execute(s)
        lst = db.fetchall()
        if lst == []:
            statement = 'insert into Content({}) values ({})'.format(
                columns, value)
            db.execute(statement, tuple(dic.values()))
        else:
            print(dic['标题'],' 已经采集过')
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


def db_execute(db_file, statement):
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    db.execute(statement)
    conn.commit()
    db.close()
    conn.close()
    print('sql is done.')
