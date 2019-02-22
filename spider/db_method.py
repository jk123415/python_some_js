#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-12
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

import sqlite3
#初始化数据库并创建数据表Content
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
    print('''start initialize database: ''',db_file)
    conn = sqlite3.connect(db_file)
    db = conn.cursor()
    db.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_name = db.fetchall()
    if ('Content',) not in table_name:
        print('create table: Content in ',db_file)
        s = post.values()
        v = ''
        for i in s:
        	c = ', '+i+' TEXT'
        	v += c
        db.execute('''CREATE TABLE Content(ID INTEGER PRIMARY KEY AUTOINCREMENT,已采 TINYINT(1),已发 TINYINT(1){})'''.format(v))
    else:
        print('already exist table: Content in ',db_file)
    conn.commit()
    conn.close()
    #print(table_name)
#更新数据库表Content字段，根据传入的列表lst    
def update_db_field(db_file,lst=[]):
	#链接数据库
	conn = sqlite3.connect(db_file)
	#创建游标
	db = conn.cursor()
	#查询Content信息
	db.execute('''PRAGMA table_info([Content])''')
	#获取查询结果
	colculmns = db.fetchall()
	#print(colculmns)
	#生成空列表lt
	lt = []
	#对查询结果进行迭代，生成lt 列名数据
	for col in colculmns:
		lt.append(col[1])
	#对传入数据lst进行迭代	
	for val in lst:
		#判断lst中的字段是否在表content中存在
		if val not in lt:
			#如果不存在，生成字段
			sta = '''ALTER TABLE Content ADD {} TEXT'''.format(val)
			print(sta)
			db.execute(sta)
			print(val,' is yes')
		else:
			#如果存在则，返回yes
			#print('yes')
			pass
	print('Table Content already update')
    conn.commit()
    conn.close()
#initialize_db(r'db_file/Nmd.db3')
#update_db_field(r'db_file/Nmd.db3',['识别代码','编号'])