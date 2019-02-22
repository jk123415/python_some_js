#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-11 16:28:43
# @Author  : leopython (hailson@sina.com)
# @Link    : http://www.cnblogs.com/leopython/
# @Version : $Id$

import os,requests,sqlite3,re
def publish34(db_file):
	post={'title':"标题",
		  'borrowid':"编号",
		  'siteid':'网站编号',
		  'lastpostdate':'时间',
		  'daystr':'借款期限',
		  'typeimg':'类型图片',
		  'posttype':'回复类型',
		  'postdata':'回复内容',
		  'money':'借款金额',
		  'rate':'年利率',
		  'senddate':'发标时间',
		  'username':'作者',
		  'jiangli':'投标奖励',
		  'jianglimoney':'奖励金额',
		  'ratetype':'利率类型',
		  'repayment_type':'还款方式',
		  'borrow_url':'网址',
		  'sex':'性别',
		  'age':'年龄',
		  'industry':'所属行业',
		  'df':'所在地',
		  'organization':'发布机构',
		  'borrow_use':'借款用途',
		  'borrower_type':'借款类别',
		  'borrow_info':'借款详情',}
	reg = re.compile('ok')
	post_uri = 'http://101.201.75.34/curl/insert.php'
	colculmus = ','.join(post.values())
	conn = sqlite3.connect(db_file)
	db = conn.cursor()
	db.execute('''SELECT {} FROM Content WHERE 已采=1 AND 已发=0'''.format(colculmus))
	#print(db.fetchall())
	lst = db.fetchall()
	if lst==[]:
		print('Need post data is 0')
		conn.close()
		return
	else:
		for postval in lst:
			publish_data = dict(zip(post.keys(),postval))
			#print(publish_data)
			rr = requests.post(post_uri,data=publish_data)
			if re.search(reg,rr.text):
				print(publish_data['title'],' issued successfull')
				db.execute('''UPDATE Content SET 已发=1 WHERE 编号="{}"'''.format(publish_data['borrowid']))
			else:
				print(publish_data['title'],' issued failed')
				db.execute('''UPDATE Content SET 已发=2 WHERE 编号="{}"'''.format(publish_data['borrowid']))
	conn.commit()
	conn.close()
#print(colculmus)
#publish34(r'C:\Users\Administrator\Desktop\spider\Test.db3')
