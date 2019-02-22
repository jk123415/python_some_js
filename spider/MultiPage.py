#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-13 10:12:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import re
import pprint


def multiPage(uri):
    lst = []

    def loopMothod(stri):
        regx = re.compile(r'(\[\d\]<\d+,\d+,\d+>)')
        regx1 = re.compile(r'(\d+)')
        if regx.search(stri):
            args = (regx.search(stri)).group()
            stri = regx.sub('%s', stri, 1)
            args1 = regx1.findall(args)
    # print(stri)
    # print(args)
    # print(args1)
            if args1[0] == '0':
                for var in range(int(args1[1]), int(args1[2]) + 1, int(args1[3])):
                    a = stri % var
                    if not regx.search(stri):
                        #global lst
                        lst.append(a)
                    loopMothod(a)
        else:
            return 'ok'
    loopMothod(uri)
    return lst


if __name__ == '__main__':
    uri = 'http://www.hulushidai.com/front//investHome?currPage=[0]<1,5,1>&pageSize=[0]<1,5,1>'
    s = multiPage(uri)
    pprint.pprint(s)
