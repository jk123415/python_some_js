import sys
sys.path.append("../..")
import os
import re
from no_vf_login import login
from queue import Queue
from threading import Thread


def auto_load(expression):
    lst = os.listdir()
    target = []
    for x in lst:
        if re.match(expression, x):
            with open(x, encoding='utf-8') as f:
                string = f.read()
                result = re.findall(r'({[\s\S]*?})', string)[0]
                t = eval(result)
                target.append(t)
    return target


def fun(q):
    while True:
        value = q.get(True)
        if value == None:
            break
        login(value)


if __name__ == '__main__':
    p_num = 8  # 同时运行的登录的数量
    q = Queue()
    threads = []
    num = auto_load('f_a_')
    for x in num:
        q.put(x)
    for x in range(p_num):
        q.put(None)
    for p in range(p_num):
        p = Thread(target=fun, args=(q,))
        p.start()
        threads.append(p)
    # 等待pw结束:
    for p in threads:
        p.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    print('end')
    # input('按回车键退出： ')
