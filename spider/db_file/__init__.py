import re
import sqlite3
dic = {'借款期限': '3个月',
       '借款用途': '用于资金周转',
       '借款金额': 200000.0,
       '发标时间': '2018-07-24',
       '回复内容': '{username=132***555|rate=9|postmoney=7780.00|money=7780.00|postdate=2018-07-26|status=全部通过}{username=186***808|rate=9|postmoney=5050.00|money=5050.00|postdate=2018-07-25|status=全部通过}{username=138***661|rate=9|postmoney=50000.00|money=50000.00|postdate=2018-07-25|status=全部通过}{username=180***990|rate=9|postmoney=5000.00|money=5000.00|postdate=2018-07-25|status=全部通过}{username=138***165|rate=9|postmoney=1250.00|money=1250.00|postdate=2018-07-25|status=全部通过}{username=138***435|rate=9|postmoney=20000.00|money=20000.00|postdate=2018-07-24|status=全部通过}{username=150***549|rate=9|postmoney=10050.00|money=10050.00|postdate=2018-07-24|status=全部通过}{username=136***446|rate=9|postmoney=20000.00|money=20000.00|postdate=2018-07-24|status=全部通过}{username=138***036|rate=9|postmoney=20220.00|money=20220.00|postdate=2018-07-24|status=全部通过}{username=156***525|rate=9|postmoney=50600.00|money=50600.00|postdate=2018-07-24|status=全部通过}',
       '完成度': '100%',
       '已采': 1,
       '年利率': '9',
       '时间': '2018-07-26',
       '标题': '保理房18032008字号09期',
       '编号': '信广财行-3262',
       '网址': 'http://www.xgcaihang.com/invest/3262.html',
       '网站编号': 8458,
       '还款方式': 4}


def update_table_data(db, dic):
    data = []
    for key, values in dic.items():
        values = "'{}'".format(values)
        f = "{}={}".format(key, values)
        data.append(f)
    a = ', '.join(data)
    b = "UPDATE Content SET {a} WHERE 网址='{link}'".format(a=a, link=dic['网址'])
    db.execute(b)
