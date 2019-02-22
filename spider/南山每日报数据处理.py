#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-13 10:38:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

with open(r'data_nansan') as f:
    x = f.readlines()
f = open(r'C:\Users\Administrator\Desktop\spider\qianjiaURI', 'w')
for id in x:
    uri = ('http://101.201.75.34/curl/list.php?siteid=' + id +
           '&day=2&ps=30&data_b=&data_e=&is_holiday=0&k=&orderby=lastpostdate&diquzs=0&search=开始搜索').replace('\n', '')
    f.write(uri + '\n')
f.close
