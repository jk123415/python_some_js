#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 18:15:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import Detailextendmodule
import sqlite3


def initialze_program(baseinfo, tag):
    print("start extract data: ", baseinfo['name'])
    Detailextendmodule.initialize_db(baseinfo['db'])
    # initizlize databases,create table Content
    Detailextendmodule.update_db_field(baseinfo['db'], tag)
    # update table Content fields


def format_headers(stri):
    if stri == '':
        return dict()
    elif isinstance(stri, str):
        a = stri.split('\n')
        data = {}
        for i in a:
            lst = i.split(": ")
            data[lst[0]] = lst[1]
        return data


def uri_handle(info, headers, base):
    links = []
    for i in range(info['varS'], info['varE'] + 1, info['varStep']):
        uri = info['sourceUri'].format(str(i))
        print('start extract list page:', uri)
        dup = 0
        if info['requestMethod'] == 'get':
            links += Detailextendmodule.get_method_link(uri, headers, info)
        else:
            # info['requestMethod'] == 'post'
            Detailextendmodule.post_method(uri, headers)
    print('extract href_num is', len(links), end=' ')
    if not info['test']:
        Detailextendmodule.save_uri(base['db'], links)


def extract_content_code(info, href, headers):
    content = []
    requestUri = href
    print('start text uri:', requestUri)
    if info['sourceCode']['requestMethod'] == 'get':
        sourceCode = Detailextendmodule.get_method_content(requestUri, headers)
        content.append(sourceCode)
    else:
        pass
    if info['associatedCode']['requestMethod'] == 'post':
        postUri = info['associatedCode']['associatedUri']
        postval = Detailextendmodule.format_postval(
            info['associatedCode']['extExp'], requestUri, info['associatedCode']['postValues'])
        associatedCode = Detailextendmodule.post_method_content(
            postUri, postval, headers)
        content.append(associatedCode)
    else:
        pass
    #print(sourceCode, associatedCode, end='\n\n\n\n')
    return content


def from_soruce_ext_data(tag_value, code):
    if tag_value['extMethod'] == 'regex':
        collectData = Detailextendmodule.regex_extract_data(
            tag_value['regexExpression'], code.text)
        if collectData and not tag_value['loopExt?']:
            return collectData[0]
        if not collectData:
            return ''
        else:
            return collectData
    elif tag_value['extMethod'] == 'xpath':
        return Detailextendmodule.xpathExtract(code.text, tag_value['xpathExpression'])
    elif tag_value['extMethod'] == 'css':
        pass


def from_source_ext_uri(tag_value, code):
    if tag_value['extMethod'] == 'regex':
        collectData = Detailextendmodule.regex_extract_data(
            tag_value['regexExpression'], code.url)
        if collectData and not tag_value['loopExt?']:
            return collectData[0]
        if not collectData:
            return ''
        else:
            return collectData
    elif tag_value['extMethod'] == 'xpath':
        return Detailextendmodule.xpathExtract(code.url, tag_value['xpathExpression'])
    elif tag_value['extMethod'] == 'css':
        pass


def from_associate_ext_data(tag_value, code):
    if tag_value['extMethod'] == 'regex':
        collectData = Detailextendmodule.regex_extract_data(
            tag_value['regexExpression'], code.text)
        if collectData and not tag_value['loopExt?']:
            return collectData[0]
        if not collectData:
            return ''
        else:
            return collectData
    elif tag_value['extMethod'] == 'xpath':
        pass
    elif tag_value['extMethod'] == 'css':
        pass


def from_tag_ext_data(tag_value, data):
    if tag_value['extMethod'] == 'regex':
        collectData = Detailextendmodule.regex_extract_data(
            tag_value['regexExpression'], data[tag_value['tagName']])
        if collectData and not tag_value['loopExt?']:
            return collectData[0]
        if not collectData:
            return ''
        else:
            return collectData
    elif tag_value['extMethod'] == 'xpath':
        return Detailextendmodule.xpathExtract(code.text, tag_value['xpathExpression'])
    elif tag_value['extMethod'] == 'css':
        pass


def datafilter(filter, data):
    for name, value in filter.items():
        if name == 'htmlTagClear' and value:
            data = Detailextendmodule.htmlTagClear(data)
        if name == 'noNone' and value:
            data = Detailextendmodule.noNone(data)
        if name == 'mustContain' and value:
            data = Detailextendmodule.mustContain(data, value)
        if name == 'noContain' and value:
            data = Detailextendmodule.noContain(data, value)
        if name == 'investRecords' and value:
            data = Detailextendmodule.investRecords(data, value)
        if name == 'regexClear' and value:
            data = Detailextendmodule.regex_clear(data, value)
        if name == 'baseHandle' and value:
            data = Detailextendmodule.base_handle(data, value)
        if name == 'amountFormat' and value:
            data = Detailextendmodule.amountformat(data)
        if name == 'payMehtodFormat' and value:
            data = Detailextendmodule.paymethodreplace(data)
        if name == 'rateFormat' and value:
            data = Detailextendmodule.rataformat(data)
    return data


def extract_data(info, sourceData):
    data = {}
    for tag_name, tag_value in info.items():
        if tag_value['sourceData'] == 'sourceCode':
            data[tag_name] = from_soruce_ext_data(tag_value, sourceData[0])
        elif tag_value['sourceData'] == 'associatedCode':
            data[tag_name] = from_associate_ext_data(tag_value, sourceData[1])
        elif tag_value['sourceData'] == 'sourceCodeUri':
            data[tag_name] = from_source_ext_uri(tag_value, sourceData[0])
        elif tag_value['sourceData'] == 'fiexdValue':
            data[tag_name] = tag_value['fiexdValue']
        elif tag_value['sourceData'] == 'tag':
            data[tag_name] = from_tag_ext_data(tag_value, data)
        data[tag_name] = datafilter(tag_value['filter'], data[tag_name])
        if data[tag_name] == 'error':
            data = {}
            return None
    data['已采'] = 1
    return data


def extract_data_test(info, sourceData):
    data = {}
    for tag_name, tag_value in info.items():
        if tag_value['sourceData'] == 'sourceCode':
            data[tag_name] = from_soruce_ext_data(tag_value, sourceData[0])
        elif tag_value['sourceData'] == 'associatedCode':
            data[tag_name] = from_associate_ext_data(tag_value, sourceData[1])
        elif tag_value['sourceData'] == 'sourceCodeUri':
            data[tag_name] = from_source_ext_uri(tag_value, sourceData[0])
        elif tag_value['sourceData'] == 'fiexdValue':
            data[tag_name] = tag_value['fiexdValue']
        elif tag_value['sourceData'] == 'tag':
            data[tag_name] = from_tag_ext_data(tag_value, data)
        data[tag_name] = datafilter(tag_value['filter'], data[tag_name])
    return data


def standar_ext_data(p, headers):
    requestUri = Detailextendmodule.get_target_uri(p)
    if requestUri:
        lst = []
        num = len(requestUri)
        print("need extract:", num)
        for href in requestUri:
            sourceData = extract_content_code(p['content'], href, headers)
            data = extract_data(p['tag'], sourceData)
            lst.append(data)
        return lst
    else:
        return None


def standar_save_data(db_file, data):
    if data:
        conn = sqlite3.connect(db_file)
        db = conn.cursor()
        for item in data:
            if item:
                Detailextendmodule.update_table_data(db, item)
        conn.commit()
        db.close()
        conn.close()
    else:
        print('extract data is 0')


def standar_publish(db_file):
    Detailextendmodule.publish_data_34(db_file)
