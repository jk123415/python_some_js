#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 18:12:50
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import Standardextendmodule
import pprint


def myfunc(p):
    baseInfo = p['base']
    uriInfo = p['uri']
    contentInfo = p['content']
    tagInfo = p['tag']
    Standardextendmodule.initialze_program(baseInfo, tagInfo)
    headers = Standardextendmodule.format_headers(baseInfo['headers'])
    Standardextendmodule.uri_handle(uriInfo, headers, baseInfo)
    if uriInfo['test']:
        return None
    if contentInfo['test']:
        sourceData = Standardextendmodule.extract_content_code(
            contentInfo, contentInfo['testUri'], headers)
        data = Standardextendmodule.extract_data_test(tagInfo, sourceData)
        print(sourceData)
        pprint.pprint(data)
    else:
        data = Standardextendmodule.standar_ext_data(p, headers)
        # print(data)
        Standardextendmodule.standar_save_data(baseInfo['db'], data)
        Standardextendmodule.standar_publish(baseInfo['db'])
