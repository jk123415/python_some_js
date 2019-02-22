
#!/usr/bin/env python
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
        'partten': 2  # 1 Synchronization acquisition ;2 extract the uri and save db first and then collect detailed imformathon
    },
    'url': {
        'sourceUri': 'http://www.xgcaihang.com/investinfo?p={}',
        'varS': 1,
        'varE': 1,
        'varStep': 1,
        'requestMethod': 'get',
        'headers?': False,
        'autoExt': True, 'mustContain': '/invest/', 'noContain': '',
        # 'manualExt': True, 'extRegex': '', 'combine': '',
        'test': False
    },
    'detali': {
        'test': {
            'state': False,
            'uri': 'http://www.xgcaihang.com/invest/3262.html'
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
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'xpath', 'selector': "//div[@class='touzwr']/h3",
            'dataHandle': {'htmlTagClear': 'yes'},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "完成度": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': 'body > div.qxWrapper > div.qxBox > div.zwj_xgch.content > div.touzye > div.toyelf > div:nth-of-type(5) > div > div > font',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '100%',
                'noContain': ''
            }
        },
        "借款金额": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "借款期限": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "年利率": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "作者": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "还款方式": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "回复内容": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "发标时间": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 3, 'values': None, 'tag': '回复内容',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "时间": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 3, 'values': None, 'tag': '回复内容',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "类型图片": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "网站编号": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "网址": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "编号": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 3, 'values': None, 'tag': '网址',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "年龄": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
        "性别": {
            # 1 source code; 2 fiexd format data ; 3 existing tag data
            'accessMethod': 1, 'values': None, 'tag': '',
            # 1 default page code; 2 associated page 1 ; 3 associated page 2;...;0 sorce uri
            'dataSource': 1,
            'extractMethod': 'css', 'selector': '',
            'dataHandle': {},
            'contentFilter': {
                'noNone': '',
                'mustContent': '',
                'noContain': ''
            }
        },
    }
}


def mydef(para):
    print("start extract ", para['base']['name'])
    essential_module.initialize_db(para['base']['db'])
    # initizlize databases,create table Content
    essential_module.update_db_field(para['base']['db'], para['tag'])
    # update table Content fields
    headers = essential_module.format_headers(para['base']['headers'])
    # format request headers info.
    for i in range(para['url']['varS'], para['url']['varE'] + 1, para['url']['varStep']):
        url = var['url']['sourceUri'].format(str(i))
        print('start extract list page:', url)
        listUrl = []
        num = 0
        dup = 0
        if para['url']['requestMethod'] == 'get':
            rep = requests.get(url, headers=headers)
            if para['url']['autoExt']:
                soup = BeautifulSoup(rep.text, "lxml")
                for linkEle in soup.find_all('a'):
                    link = str(linkEle.get('href'))
                    if re.match(para['url']['mustContain'], link):
                        if para['url']['noContain']:
                            if not re.match(para['url']['noContain'], link):
                                if re.match('/', link):
                                    g = re.match(
                                        '(^.*com)', para['url']['sourceUri'])
                                    link = g[0] + link
                                    listUrl.append(link)
                                    num += 1
                        else:
                            if re.match('/', link):
                                g = re.match(
                                    '(^.*com)', para['url']['sourceUri'])
                                link = g[0] + link
                                listUrl.append(link)
                                num += 1
        else:
            pass
        if listUrl:
            conn = sqlite3.connect(para['base']['db'])
            db = conn.cursor()
            for i in listUrl:
                s = 'select * from Content where 网址="%s"' % i
                db.execute('select * from Content where 网址="%s"' % i)
                if db.fetchall():
                    dup += 1
                else:
                    if not para['url']['test']:
                        db.execute(
                            'insert into Content (网址) values ("%s")' % i)
            conn.commit()
            db.close()
            conn.close()
        pprint.pprint(listUrl)
        print('extract links num is', num, ',duplicate is ',
              dup, 'new links is', num - dup)
    if para['url']['test']:
        exit()
    if para['base']['partten'] == 2:
        conn = sqlite3.connect(para['base']['db'])
        db = conn.cursor()
        db.execute("select 网址 from Content where 已采 is null")
        l = db.fetchall()
        targetUrl = []
        if l:
            for x in l:
                targetUrl.append(x[0])
            print('need collected data is', len(targetUrl))
            for x in targetUrl:
                if para['detali']['test']['state']:
                    requestUrl = para['detali']['test']['uri']
                else:
                    requestUrl = x
                print('start requests Uri:', requestUrl)
                if para['detali']['content']['requestMethod'] == 'get':
                    page = requests.get(requestUrl, headers=headers)
                    print(page.status_code)
                    if para['detali']['associate']['requestMethod'] == 'post':
                        s = re.search(
                            para['detali']['associate']['rule'], requestUrl)
                        source = re.sub(
                            'variable_a', s[1], para['detali']['associate']['postval'])
                        data = essential_module.format_postval(source)
                        print('start requests associated uri: ',
                              para['detali']['associate']['posturi'], data)
                        associatedPage = requests.post(
                            para['detali']['associate']['posturi'], data=data, headers=headers)
                        print(associatedPage.status_code)
                    else:
                        # get method ----------------------------------------------
                        pass
                    entry = {}
                    if para['detali']['content']['pageAttribute'] == 'html':
                        html = etree.HTML(page.text)
                        soup = BeautifulSoup(page.text, 'lxml')
                    else:
                        # para['detali']['content']['pageAttribute'] == 'json':
                        pass
                    for tag_name, tag_rule in para['tag'].items():
                        if tag_rule['accessMethod'] == 1:
                            if tag_rule['dataSource'] == 1:
                                if tag_rule['extractMethod'] == 'css':
                                    try:
                                        if para['detali']['test']['state']:
                                            if not tag_rule['selector']:
                                                entry[tag_name] = None
                                            else:
                                                if soup.select(tag_rule['selector']):
                                                    temporary_a = ''
                                                    for i in soup.select(tag_rule['selector']):
                                                        temporary_a += i.text
                                                    entry[tag_name] = temporary_a
                                        else:
                                            if soup.select(tag_rule['selector']):
                                                temporary_a = ''
                                                for i in soup.select(tag_rule['selector']):
                                                    temporary_a += i.text
                                                entry[tag_name] = temporary_a
                                            else:
                                                entry[tag_name] = None
                                    except NotImplementedError:
                                        print(
                                            tag_name, ' css selector is error, please change "nth-child" to "nth-of-type"')
                                        exit()
                                else:
                                    # tag_rule['extractMethod'] == 'xpath':
                                    if html.xpath(tag_rule['selector']):
                                        result = ''
                                        for ele in html.xpath(tag_rule['selector']):
                                            result += ele.text
                                        if tag_rule['dataHandle']['htmlTagClear'] == 'yes':
                                            result = re.subn(
                                                r'[\s\r\n]', '', result)[0]
                                        entry[tag_name] = result
                                    else:
                                        entry[tag_name] = None
                            elif tag_rule['dataSource'] == 2:
                                pass
                            else:
                                # tag_rule['dataSource'] == 3:
                                pass
                            if tag_rule['contentFilter']['noNone']:
                                if not entry[tag_name]:
                                    if para['detali']['test']['state']:
                                        entry[tag_name] = 'do not satisfy the necessary conditions--noNone'
                                        print(requestUrl, '\n', tag_name,
                                              ' extract result is None')
                                    else:
                                        print(requestUrl, '\n', tag_name,
                                              ' extract result is None')
                                        next
                            if tag_rule['contentFilter']['mustContent']:
                                f = re.match(
                                    tag_rule['contentFilter']['mustContent'], entry[tag_name])
                                if not f:
                                    print(
                                        requestUrl, '\n', tag_name, 'do not satisfy the necessary conditions--mustContent')
                                    if para['detali']['test']['state']:
                                        entry[tag_name] = None
                                    else:
                                        next
                            if tag_rule['contentFilter']['noContain']:
                                pass
                            # print(entry[tag_name])
                        elif tag_rule['accessMethod'] == 2:
                            pass
                        else:
                            # tag_rule['accessMethod']==3
                            pass
                    # ----------------------------------------------------
                    print(entry)
                else:
                    # post method------------------------------------------------------
                    pass
                if para['detali']['test']['state']:
                    exit()
        else:
            print('need collected data is 0')
        conn.commit()
        db.close()
        conn.close()


mydef(var)
