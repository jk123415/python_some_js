#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-08 13:41:29
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import essential_module
import pprint
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import sqlite3

var = {
    'base': {
        "name": '信广财行',
        "db": r'C:\Users\Administrator\Desktop\spider\db_file\XGCH.db3',
        "headers": '''''',
        'partten': 1   # 2 Synchronization acquisition ;1 extract the uri and save db first and then collect detailed imformathon
    },
    'uri': {
        'sourceUri': 'http://www.xgcaihang.com/investinfo?p={}',
        'varS': 1,
        'varE': 2,
        'varStep': 1,
        'requestMethod': 'get',
        'headers?': False,
        'autoExt': True, 'mustContain': '/invest/', 'noContain': '',
        #'manualExt': True, 'extRegex': '', 'combine': '',
        'test': False
    },
    'detali': {
        'test': {
            'state': False,
            'uri': 'http://www.xgcaihang.com/invest/3244.html'
        },
        'content': {
            'requestMethod': 'get',
            'pageAttribute': 'html'
        },
        'associate': {
            'requestMethod': 'post',
            'posturi': 'http://www.xgcaihang.com/home/investinfo/investlog',
            'rule': 'http://www.xgcaihang.com/invest/(\w+).html',
            'postval': 'borrow_id=variable_a',
            'associated': []
        },
    },
    'tag': {
        "标题": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': "//div[@class='touzwr']/h3",
            'dataHandle': {},
            'contentFilter': {
                'htmlTagClear': True,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "完成度": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': '//div/font',
            'dataHandle': {},
            'contentFilter': {
                'htmlTagClear': True,
                'noNone': True,
                'mustContain': '100%',
                'noContain': ''
            }
        },
        "回复内容": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 2,
            'extractMethod': 'regex', 'selector': r'<p>(.*?)<\/p>\r\n            <\/div>\r\n\r\n            <div class=\"tdiv2\">\r\n                (.*?)%\r\n            <\/div>\r\n            <div class=\"tdiv2\">\r\n                (.*?)\u5143\r\n            <\/div>\r\n            <div class=\"tdiv1\">\r\n                (.*?)            <\/div>\r\n',
            'dataHandle': "{{username={list[0]}|rate={list[1]}|postmoney={list[2]}|money={list[2]}|postdate={list[3]}|status=全部通过}}",
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "借款金额": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': '//div[@class="touzye"]/div[@class="toyelf"]/div[5]/span',
            'dataHandle': {},
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': '',
                'amountformat': True
            }
        },
        "借款期限": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': '/html/body/div[1]/div[1]/div[8]/div[2]/div[1]/div[3]/span',
            'dataHandle': {},
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "年利率": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': '/html/body/div[1]/div[1]/div[8]/div[2]/div[1]/div[1]/span/text()',
            'dataHandle': {},
            'contentFilter': {
                'htmlTagClear': True,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "还款方式": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': '/html/body/div[1]/div[1]/div[8]/div[2]/div[1]/div[3]/div/span[2]',
            'dataHandle': "",
            'contentFilter': {
                'htmlTagClear': True,
                'noNone': True,
                'mustContain': '',
                'noContain': '',
                'paymethodreplace': True
            }
        },
        "借款用途": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': '//*[@id="tabco"]/span[1]/div/div/div[2]/div[2]/p',
            'dataHandle': {},
            'contentFilter': {
                'htmlTagClear': True,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "发标时间": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 3, 'values': None, 'tag': '回复内容',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'regex', 'selector': r'{.*postdate=(.*?)\|status=全部通过}$',
            'dataHandle': "{list[0]}",
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "时间": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 3, 'values': None, 'tag': '回复内容',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'regex', 'selector': r'{.*?postdate=(.*?)\|status=全部通过}.*',
            'dataHandle': "{list[0]}",
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "网址": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data ; 4 请求网址
            'accessMethod': 4, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': '', 'selector': "",
            'dataHandle': "",
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "编号": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 3, 'values': None, 'tag': '网址',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'regex', 'selector': r'/invest/(\w+).html',
            'dataHandle': "信广财行-{list[0]}",
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "网站编号": {
            # 1 lxml page; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 2, 'values': 8458, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': '', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'htmlTagClear': False,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
    }
}


def myfunc(p):
    p_one = p['base']
    print("start extract ", p_one['name'])
    essential_module.initialize_db(p_one['db'])
    # initizlize databases,create table Content
    essential_module.update_db_field(p_one['db'], p['tag'])
    # update table Content fields
    headers = essential_module.format_headers(p_one['headers'])
    # format request headers info.
    p_two = p['uri']
    for i in range(p_two['varS'], p_two['varE'] + 1, p_two['varStep']):
        uri = p_two['sourceUri'].format(str(i))
        print('start extract list page:', uri)
        listUri = []
        num = 0
        dup = 0
        if p_two['requestMethod'] == 'get':
            rep = requests.get(uri, headers=headers)
            if p_two['autoExt']:
                page = etree.HTML(rep.text)
                links = page.xpath(u"//a")
                for link in links:
                    href = link.get('href')
                    if not href:
                        continue
                    if re.match(p_two['mustContain'], href):
                        # must contain handle
                        if p_two['noContain']:
                            # no contain != ''
                            if not re.match(p_two['noContain'], href):
                                # href no contain handle
                                if re.match('/', href):
                                    g = re.match(
                                        '(^.*com)', p_two['sourceUri'])
                                    href = g[0] + href
                                    listUri.append(href)
                                    num += 1
                        else:
                            # p_two['noContain']== ''
                            if re.match('/', href):
                                g = re.match('(^.*com)', p_two['sourceUri'])
                                href = g[0] + href
                                listUri.append(href)
                                num += 1
                pass
            else:
                # p_two['autoExt'] == False
                pass
            pass
        else:
            # p_two['requestMethod'] == 'post':
            pass
        if p_two['test']:
            print('start test extract uri: ')
            pprint.pprint(listUri)
            exit()
        if listUri:
            # listUri != ''
            conn = sqlite3.connect(p_one['db'])
            db = conn.cursor()
            for n in listUri:
                a = 'select * from Content where 网址="%s"' % n
                db.execute(a)
                if db.fetchall():
                    # The results of the query isn't []
                    dup += 1
                else:
                    # The results of the query is []
                    if not p_two['test']:
                        # uri isn't test
                        db.execute(
                            'insert into Content (网址) values ("%s")' % n)
            conn.commit()
            db.close()
            conn.close()
            pprint.pprint(listUri)
            print('extract links num is', num, ',duplicate is',
                  dup, ', new links is', num - dup)
        else:
            # listUri == []
            print('extract link is 0,please check the parameter code')
    p_three = p['detali']
    if p_one['partten'] == 1:
        conn = sqlite3.connect(p_one['db'])
        db = conn.cursor()
        db.execute("select 网址 from Content where 已采 is null")
        b = db.fetchall()
        targetUri = []
        if b:
            # b != []
            for m in b:
                if p_three['test']['state']:
                    # extract detail test is True
                    requestUri = p_three['test']['uri']
                else:
                    # extract detail test is False
                    requestUri = m[0]
                print('start requests Uri:', requestUri, end=' ')
                if p_three['content']['requestMethod'] == 'get':
                    # content page request method is get
                    page = requests.get(requestUri, headers=headers)
                    print(page.status_code)
                    pass
                else:
                    # content page request method is post , api is contentpage
                    pass
                contentpage = page.text
                # content page reponse body
                associatepage = []
                if p_three['associate']['requestMethod'] == 'post':
                    # associated page request method is post, api associatepage
                    c = re.search(p_three['associate']['rule'], requestUri)
                    source = re.sub(
                        'variable_a', c[1], p_three['associate']['postval'])
                    data = essential_module.format_postval(source)
                    print('start requests associated uri: ',
                          p_three['associate']['posturi'], data, end=' ')
                    d = requests.post(p_three['associate']['posturi'],
                                      data=data, headers=headers)
                    print(d.status_code)
                    associatepage.append(d)
                else:
                    # associated page request method is get, api associatepage
                    pass
                # ------------------------------------------------------------------------
                # start tag loop handle
                entry = {}
                # initialize target data
                p_four = p['tag']
                lxmlpage = etree.HTML(contentpage)
                terminationloop = False
                for x, y in p_four.items():
                    entry[x] = None
                    if y['accessMethod'] == 1:
                        # lxml page extract data
                        if y['dataSource'] == 1:
                            # default source contentpage lxml page
                            if y['extractMethod'] == 'xpath':
                                # extract method is xpath
                                e = lxmlpage.xpath(y['selector'])
                                if e:
                                    # xpath extract data isn't []
                                    try:
                                        f = ''
                                        for z in e:
                                            f += z.xpath('string(.)')
                                    except AttributeError:
                                        g = ''.join(e)
                                        f = g
                                    entry[x] = f
                                else:
                                    # xpath extract data is []
                                    entry[x] = None
                            elif y['extractMethod'] == 'css':
                                # extract method is css
                                pass
                        elif y['dataSource'] == 2:
                            # associated page 1
                            sourcecode = associatepage[0].text
                            if y['extractMethod'] == 'regex':
                                g = re.subn(r'[\\]', r'\\\\', y['selector'])
                                h = re.findall(g[0], sourcecode)
                                if h:
                                    # match data is not []
                                    j = ''
                                    for k in h:
                                        j += y['dataHandle'].format(list=k)
                                    entry[x] = j
                                else:
                                    # match data is []
                                    entry[x] = None
                            elif y['extractMethod'] == 'xpath':
                                pass
                    elif y['accessMethod'] == 2:
                        # fiexd format data
                        entry[x] = y['values']
                    elif y['accessMethod'] == 3:
                        # existing tag data
                        if y['extractMethod'] == 'regex':
                            try:
                                aa = re.findall(y['selector'], entry[y['tag']])
                                entry[x] = y['dataHandle'].format(list=aa)
                            except IndexError:
                                print(x, '-regex express is error')
                                entry[x] = None
                    elif y['accessMethod'] == 4:
                        entry[x] = requestUri
                    # --------------------------------------
                    # handle Acquired data
                    for extendname, extendvalue in y['contentFilter'].items():
                        # loop content Filter
                        if entry[x]:
                            # extract data isn't none
                            if extendname == 'htmlTagClear' and extendvalue:
                                clearstr = re.compile(r'[\s\r\n\t]')
                                entry[x] = clearstr.subn('', entry[x])[0]
                        if extendname == 'noNone' and extendvalue:
                            if not entry[x]:
                                terminationloop = True
                                entry[x] = 'can not be empty'
                                print(x, "error--noNone")
                                break
                        if extendname == 'mustContain' and extendvalue:
                            mustcontainstr = re.compile(extendvalue)
                            if not mustcontainstr.match(entry[x]):
                                entry[x] = 'do not satisfy the necessary conditions--mustContain'
                                terminationloop = True
                                print(x, "error--mustContain")
                                break
                        if extendname == 'paymethodreplace' and extendvalue:
                            entry[x] = essential_module.paymethodreplace(
                                entry[x])
                        if extendname == 'amountformat' and extendvalue:
                            entry[x] = essential_module.amountformat(entry[x])
                    # print(entry[x])
                    if terminationloop:
                        break
                entry['已采'] = 1
                if p_three['test']['state']:
                    # extract detail test is True,stop loop
                    pprint.pprint(entry)
                    break
                if not terminationloop:
                    essential_module.update_table_data(db, entry)
        else:
            # b == []
            print('new need extract detail info is 0')
        conn.commit()
        db.close()
        conn.close()
    else:
        # p_one['partten'] == 2
        pass
    essential_module.publish_data_34(p_one['db'])


myfunc(var)
