#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-12 17:34:09
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re
import json
import pprint
import sqlite3
import jsonpath
import requests
import lxml.html


def form_data(stri):
    if stri == '':
        return {}
    elif isinstance(stri, str):
        a = stri.split('&')
        data = {}
        for i in a:
            lst = i.split('=')
            data[lst[0]] = lst[1]
        return data
    elif isinstance(stri, dict):
        return stri
    else:
        pass
# 请求主体处理return a dict


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
# 头消息处理


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
# 初始化数据库生成Content表


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
# 更新数据库Content表列名，根据传入的lst


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
# 根据传入的字典更新数据库Content表信息


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
# 发布数据方法
#===============================================================================================================


class Tag(object):
    def __init__(self, tag_val, arg):
        exname = tag_val['extend']
        self.name = tag_val['name']
        self.value = tag_val['value']
        if exname == {}:
            pass
        else:
            for key, value in exname.items():
                if key == 'jsonpath':
                    try:
                        self.value = (jsonpath.jsonpath(
                            arg, expr=value))[0]
                    except:
                        print(self.name, '--extend:jsonpath is error.')
                elif key == 'math':
                    try:
                        if exname['math'][1] == '/':
                            # print('yes')
                            v1 = jsonpath.jsonpath(arg, expr=value[0])[0]
                            v2 = jsonpath.jsonpath(arg, expr=value[2])[0]
                            self.value = float(v1) / float(v2)
                    except:
                        print(self.name, '--插件math is error')
                elif key == 'mustcondi':
                    try:
                        if float(self.value) != float(value):
                            self.value = 'no'
                        # print(self.value)
                    except:
                        print(self.name, '--插件mustcondi is error')
                # 还款方式替换 replace
                elif key == 'replace':
                    try:
                        for i in range(len(value)):
                            # print(value[i])
                            if str(self.value) == str(value[i][0]):
                                self.value = value[i][1]
                    except:
                        print(self.name, '--插件replace is error')
                # 回复类容替换
                elif key == 'loop_match_investrecords':
                    try:
                        investlist = ''
                        for ety in self.value:
                            stri = '{{username={0}|rate={1}|postmoney={2}|money={2}|postdate={3}|status=全部通过}}'.format(
                                ety[value[0]], value[1], ety[value[2]], ety[value[3]])
                            investlist += stri
                        self.value = investlist
                    except:
                        print(self.name, '--插件loop_match_investrecords is error')


class Entry(object):
    def __init__(self, var, arg):
        # 对于每一条数arg，循环处理tag，生成相应的tag对象
        # 采集page_0的数据
        # print(var['tag'])
        # pprint.pprint(arg)
        # 收集采集数据生成 data字典数据
        data = {}
        for tag, val in var['tag'].items():
            t = Tag(val, arg)
            dic = getattr(t, '__dict__')
            data[dic['name']] = dic['value']
        # print(data)
        self.data = data
        pass


class Spyder(object):
    def __init__(self):
        self.var = {}

    def spider(self):
        var = self.var
        # 初始化数据库
        initialize_db(var['base']['db_file'])
        # 处理请求头
        headers = header(var['base']['headers'])
        # 处理请求主体
        for page in range(var['base']['data'][0][0], var['base']['data'][0][1]):
            body = var['base']['data'][1].format(page)
            data_0 = form_data(body)
            # 开始请问数据
            resp_body_0 = json.loads(requests.post(
                var['base']['uri'], data=data_0).text)
            # pprint.pprint(resp_body_0)
            # 获取items数据,根据路径
            try:
                for key in var['base']['path']:
                    resp_body_0 = resp_body_0[key]
                items = resp_body_0
                # pprint.pprint(items)
            except:
                print('列表数据请求错误，联系技术人员')
                exit()
            # 处理列表数据
            for entry in items:
                # 生成ety对象
                # print(var['page_0'])
                ety = Entry(var['page_0'], entry)
                # print(entry)
                # print(ety.data)
                # 完成度判断是否为no
                if ety.data['完成度'] == 'no':
                    print(ety.data['标题'], ' 未完成不采集')
                    continue
                # 处理内容页请求主体
                data_1 = var['page_1']['data'][0].format(
                    ety.data[var['page_1']['data'][1]])
                # print(data_1)
                # 获取内容页响应主体
                # print(var['page_1']['uri'])
                resp_body_1 = json.loads(requests.post(
                    var['page_1']['uri'], data=data_1, headers=headers).text)
                # pprint.pprint(resp_body_1)
                ety_1 = Entry(var['page_1'], resp_body_1)
                # 合并标签数据
                items = dict(ety.data, **ety_1.data)
                # print(items)
                # 借款期限处理
                items['借款期限'] = str(items['借款期限']) + items['借款期限类型']
                # 年利率处理
                items['年利率'] = float(items['年利率']) + float(items['年利率奖励'])
                # 编号处理
                items['编号'] = var['base']['website_name'] + \
                    '-' + str(items['识别代码'])
                # 网址处理
                items['网址'] = var['base']['detail_uri'].format(items['识别代码'])
                # 已采与已发处理
                items['已采'] = 1
                items['已发'] = 0
                #print(items)
                # 入库处理
                # 根据标签名更新数据库字段
                # cols = list(items.keys())========================================================
                # print(cols)
                # update_db_field(var['base']['db_file'], cols)================================
                # 更新数据库
                update_db(var['base']['db_file'], items)
                # 发布处理
                #break
            #break
        publish34(var['base']['db_file'])
        pass


spyder = Spyder()

spyder.var = {
    'base': {'db_file': r'C:\Users\Administrator\Desktop\spider\db_file\Hch.db3',
             'uri': 'https://www.daicaihang.com/api/Lend/pcbidlist.html',
             'headers': '''Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 7
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: init_refer=http%3A%2F%2F101.201.208.237%3A81%2Fcurl%2Flist.php%3Fsiteid%3D3186%26day%3D%26ps%3D30%26data_b%3D2018-05-01%26data_e%3D2018-06-04%26is_holiday%3D0%26k%3D%26orderby%3Dlastpostdate%26diquzs%3D0%26search%3D%25E5%25BC%2580%25E5%25A7%258B%25E6%2590%259C%25E7%25B4%25A2; UM_distinctid=163c8d4bb55715-0e23958e9a292-44410a2e-100200-163c8d4bb56e3c; Qs_lvt_185697=1528082774%2C1529377476%2C1529377494%2C1529895487%2C1530082331; CNZZDATA1254766663=698215885-1528081706-null%7C1530082144; _jzqa=1.2586340903282471400.1528082775.1529895488.1530082331.4; _jzqx=1.1528082775.1530082331.3.jzqsr=101%2E201%2E208%2E237:81|jzqct=/curl/list%2Ephp.jzqsr=openurls%2Ecom%2Ecn|jzqct=/; Qs_pv_185697=1782475151439741200%2C1542816128905880000%2C2705452756653087000%2C1831851016722049500%2C1576750729920283400; _qzja=1.2032280247.1528082774911.1529895487569.1530082331345.1530082528639.1530082534321.0.0.0.14.4; aliyungf_tc=AQAAAC/g1AmKZwsAg0ZZcbucfyr40qGY; PHPSESSID=b7r6sg81pn08j2sf4karvj0hi1; Hm_lvt_0aa1c9d29328129072b71d8c53768965=1530082331,1531387988,1531389736,1531719866; Hm_lpvt_0aa1c9d29328129072b71d8c53768965=1531720134; SERVERID=3fc065e1d1fc5abf674558eb9406795b|1531720446|1531719864
Host: www.daicaihang.com
Origin: https://www.daicaihang.com
Referer: https://www.daicaihang.com/index/lend/lend_detail.html?id=6414
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
X-Requested-With: XMLHttpRequest''',
             'data': ((1, 5), 'p={}&ep=5&cate=&date=&apr='),
             'path': ('data', 'data'),
             'website_name': '贷财行',
             'detail_uri': 'https://www.daicaihang.com/index/lend/lend_detail.html?id={}'},
    'page_0': {'uri': None,
               'tag': {'title': {'name': '标题', 'value': None, 'extend': {'jsonpath': '$.title', }},
                       'rate': {'name': '年利率', 'value': None, 'extend': {'jsonpath': '$.apr', }},
                       'amount': {'name': '借款金额', 'value': None, 'extend': {'jsonpath': '$.amount', }},
                       'date': {'name': '借款期限', 'value': None, 'extend': {'jsonpath': '$.date', }},
                       'date_type': {'name': '借款期限类型', 'value': None, 'extend': {'jsonpath': '$.dateType', }},
                       'id': {'name': '识别代码', 'value': None, 'extend': {'jsonpath': '$.id', }},
                       'rate_1': {'name': '年利率奖励', 'value': None, 'extend': {'jsonpath': '$.jx', }},
                       'progress': {'name': '完成度', 'value': None, 'extend': {'jsonpath': '$.last_money',
                                                                             'mustcondi': '0'}}, }, },
    'page_1': {'uri': 'https://www.daicaihang.com/api/Lend/bidinfo.html',
               'data': ('id={}', '识别代码'),
               'tag': {'borrower': {'name': '作者', 'value': None, 'extend': {'jsonpath': '$..realname', }},
                       'paytype': {'name': '还款方式', 'value': None, 'extend': {'jsonpath': '$..paytype', 'replace': ((3, 4), (2, 2))}},
                       'start_time': {'name': '发标时间', 'value': None, 'extend': {'jsonpath': '$..start_time', }},
                       'website_id': {'name': '网站编号', 'value': 3186, 'extend': {}},
                       'investrecords': {'name': '回复内容', 'value': None, 'extend': {'jsonpath': '$.data.arTen',
                                                                                   'loop_match_investrecords': ('cust_name', -1, 'tranamt', 'addtime')}},
                       'time': {'name': '时间', 'value': None, 'extend': {'jsonpath': '$.data.arTen[0].addtime', }},
                       }, },
    'page_2': {'uri': None,
               'tag': {}, },
}
# 开始请求数据
spyder.spider()
