#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-09 18:53:56
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : 1.1

import pprint
import Standardmodule

var = {
    'base': {
        "name": '星金所',
        "db": r'C:\Users\Administrator\Desktop\spider\db_file\XJS.db3',
        "headers": '''''',
        'partten': 1
        # 2 Synchronization acquisition ;1 extract the uri and save db first
        # and then collect detailed imformathon
    },
    'uri': {
        'varS': 1,
        'varE': 1,
        'varStep': 1,
        #'sourceUri': 'http://www.xjswe.com/financing/sbtz/index.htm?currentPage={}&pageSize=10&bidType=&yearRate=&progress=&status=&orderItem=',
        'sourceUri': 'http://www.xjswe.com/financing/sbtz/grlb.htm?currentPage={}&pageSize=10&bidType=&yearRate=&creditTerm=&status=&orderItem=',
        'requestMethod': 'get',
        'uriExtMethod': 'manualExt',
        # autoExt ; manualExt
        'extExp': r'"F02":(\w+),',
        'resultUri': 'http://www.xjswe.com/financing/sbtz/bdxq/{}.html',
        'mustContain': '',
        'noContain': '',
        # 'manualExt': True, 'extRegex': '', 'combine': '',
        'test': False
    },
    'content': {
        'test': False,
        'testUri': 'http://www.xjswe.com/financing/sbtz/bdxq/496.html',
        'sourceCode': {
            'requestMethod': 'get'
        },
        'associatedCode': {
            'requestMethod': 'post',
            'extExp': r'http://www.xjswe.com/financing/sbtz/bdxq/(\w+).html',
            'postValues': 'type=tzjl&id={}&pageSize=100&currentPage=1',
            'associatedUri': 'http://www.xjswe.com/financing/sbtz/bdxqData.htm'
        }
    },
    'tag': {
        "标题": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '/html/body/div[3]/div[1]/div[1]/div[1]/span',
            'regexExpression': r'',
            'loopExt?': False,
            'filter': {
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "完成度": {
            'sourceData': 'sourceCode',
            'extMethod': 'regex',
            'regexExpression': r'投资进度：<span class="remainAmount"></span>%<span class="hideAmount" style="font-size:0px;">(.*?)</span>',
            'loopExt?': False,
            'filter': {
                'noNone': '',
                'mustContain': '',
                'noContain': ''
            }
        },
        "年利率": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '/html/body/div[3]/div[1]/div[1]/div[2]/ul/li[2]/div[1]/span',
            'loopExt?': False,
            'filter': {
                'rateFormat': True,
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "回复内容": {
            'sourceData': 'associatedCode',
            'extMethod': 'regex',
            'regexExpression': r'{.*?,"F04":(.*?),.*?,"F06":(.*?)000,.*?,"F10":"(.*?)",.*?}',
            'loopExt?': True,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "{{username={t[2]}|rate=-1|postmoney={t[0]}|money={t[0]}|postdate={t[1]}|status=全部通过}}",
                'regexClear': r'',
                'noNone': True
            }
        },
        "还款方式": {
            'sourceData': 'sourceCode',
            'extMethod': 'regex',
            'xpathExpression': '/html/body/div[3]/div[1]/div[1]/div[2]/ul/li[4]',
            'regexExpression': r'还款方式：</span><span>(.*?)<',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'payMehtodFormat': True,
                'noNone': True
            }
        },
        "作者": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '//*[@id="dataHtml"]/div[2]/ul/div/span[1]',
            'regexExpression': '',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': ''
            }
        },
        "借款期限": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '/html/body/div[3]/div[1]/div[1]/div[2]/ul/li[2]/div[2]/div/div/span',
            'regexExpression': '',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': True
            }
        },
        "借款金额": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '/html/body/div[3]/div[1]/div[1]/div[2]/ul/li[1]/div/span',
            'regexExpression': '',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'amountFormat': True,
                'noNone': True
            }
        },
        "所在地": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '/html/body/div[2]/div/div[2]/div/div[1]/div/table[1]/tbody/tr[2]/td[4]',
            'regexExpression': '',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': ''
            }
        },
        "类型图片": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/p/span',
            'regexExpression': '',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': "",
            }
        },
        "网址": {
            'sourceData': 'sourceCodeUri',
            'extMethod': 'regex',
            'xpathExpression': '',
            'regexExpression': '^(.*)$',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': True
            }
        },
        "编号": {
            'sourceData': 'sourceCodeUri',
            'extMethod': 'regex',
            'xpathExpression': '',
            'regexExpression': r'/bdxq/(\w+).html',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'baseHandle': '星金所-参数',
                'noNone': True
            }
        },
        "网站编号": {
            'sourceData': 'fiexdValue',
            'fiexdValue': '5430',
            'extMethod': '',
            'xpathExpression': '',
            'regexExpression': '',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': True
            }
        },
        "发标时间": {
            'sourceData': 'tag',
            'tagName': '回复内容',
            'extMethod': 'regex',
            'xpathExpression': '',
            'regexExpression': r'{.*postdate=(.*?)\|status=全部通过}$',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': True
            }
        },
        "时间": {
            'sourceData': 'tag',
            'tagName': '回复内容',
            'extMethod': 'regex',
            'xpathExpression': '',
            'regexExpression': r'{.*?postdate=(.*?)\|status=全部通过}.*',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'noNone': True
            }
        }
    }
}

Standardmodule.myfunc(var)
