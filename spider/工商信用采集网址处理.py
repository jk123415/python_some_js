#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-08 18:24:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


with open(r'C:\Users\Administrator\Desktop\企业分类培训\天眼查采集网址.txt') as f:
    x = f.readlines()
f = open(r'C:\Users\Administrator\Desktop\企业分类培训\天眼查采集网址.txt', 'w')
for id in x:
    uri = ('https://www.tianyancha.com/search?key=' + id).replace('\n', '')
    print(uri)
    f.write(uri + '\n')
f.close
