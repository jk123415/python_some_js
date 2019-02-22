#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-09 18:53:56
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : 1.0

import pprint
import Standardmodule

var = {
    'base': {
        "name": '创宇贷',
        "db": r'C:\Users\Administrator\Desktop\spider\db_file\CYD.db3',
        "headers": '''''',
        'partten': 1
        # 2 Synchronization acquisition ;1 extract the uri and save db first and then collect detailed imformathon
    },
    'uri': {
        'varS': 1,
        'varE': 1,
        'varStep': 1,
        'sourceUri': 'http://www.chuangyudai.com/product/list/{}?preMonth=0&endMonth=0&yearIncome=0',
        'requestMethod': 'get',
        'uriExtMethod': 'manualExt',
        # autoExt ; manualExt
        'extExp': r'"id":(\w+),',
        'resultUri': 'http://www.chuangyudai.com/product/detail/{}',
        'mustContain': '',
        'noContain': '',
        #'manualExt': True, 'extRegex': '', 'combine': '',
        'test': False
    },
    'content': {
        'test': False,
        'testUri': 'http://www.chuangyudai.com/product/detail/30',
        'sourceCode': {
            'requestMethod': 'get'
        },
        'associatedCode': {
            'requestMethod': 'post',
            'extExp': r'http://www.chuangyudai.com/product/detail/(\w+)',
            'postValues': 'productId={}&page=1',
            'associatedUri': 'http://www.chuangyudai.com/product/latestBuyDetail'
        }
    },
    'tag': {
        "标题": {
            'sourceData': 'sourceCode',
            'extMethod': 'regex',
            'regexExpression': r'<title>(\w+)</title>',
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
                'noNone': True,
                'mustContain': '100',
                'noContain': ''
            }
        },
        "年利率": {
            'sourceData': 'sourceCode',
            'extMethod': 'regex',
            'regexExpression': r'id="yearIncome">(.*?)</span>%',
            'loopExt?': False,
            'filter': {
                'noNone': True,
                'mustContain': '',
                'noContain': ''
            }
        },
        "回复内容": {
            'sourceData': 'associatedCode',
            'extMethod': 'regex',
            'regexExpression': r'{"customerName":"(.*?)","principal":(.*?),"cellphone":"(.*?)","name":"(.*?)","orderTime":"(.*?)\s.*?}',
            'loopExt?': True,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "{{username={t[0]}|rate=-1|postmoney={t[1]}|money={t[1]}|postdate={t[4]}|status=全部通过}}",
                'regexClear': r'',
                'noNone': True
            }
        },
        "还款方式": {
            'sourceData': 'sourceCode',
            'extMethod': 'xpath',
            'xpathExpression': '/html/body/div[2]/div/div[1]/div[1]/p/span',
            'regexExpression': '',
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
            'xpathExpression': '/html/body/div[2]/div/div[2]/div/div[1]/div/table[1]/tbody/tr[1]/td[2]',
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
            'xpathExpression': '/html/body/div[2]/div/div[1]/div[1]/div[1]/div[3]/p',
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
            'xpathExpression': '/html/body/div[2]/div/div[2]/div/div[1]/ul/li[4]/p',
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
            'regexExpression': r'detail/(\w+)',
            'loopExt?': False,
            'filter': {
                'htmlTagClear': False,
                'mustContain': '',
                'noContain': '',
                'investRecords': "",
                'regexClear': '',
                'baseHandle': '创宇贷-参数',
                'noNone': True
            }
        },
        "网站编号": {
            'sourceData': 'fiexdValue',
            'fiexdValue': '8192',
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
