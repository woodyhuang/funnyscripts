#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import csv
import codecs

SIZE = 4000000  # max rows in excel2003 and excel2007 are 65535 and 1048576


def outputs(str):
    try:
        print str.decode('utf-8')
    except:
        print 'ERROR~~ while outputs'


COMMA = u'，'.encode('utf-8')
QUOTES = u'“'.encode('utf-8')
SINGLE_QUOTES = u'‘'.encode('utf-8')
def row_wrapper(row, coding='utf-8'):
    for i, c in enumerate(row):
        try:
            #row[i] = c.strip().decode(coding)
            # 转义掉特殊字符，因为客户直接用编辑器导入 :(
            if c.find(',') > -1:
                outputs('convet COMMA for: %s' % c)
                c = c.replace(',', COMMA)
            #if c.find('"') > -1:
            #    c = c.replace('"', QUOTES)
            #if c.find("'") > -1:
            #    c = c.replace("'", SINGLE_QUOTES)
            row[i] = c
        except:
            outputs('ERROR wrapper for str: %s' %c)
            raise
    return row


def file_writer(fname, parts):
    name, ext = os.path.splitext(fname)
    target = open(('%s-part.%d%s'%(name, parts, ext)),'w')
    target.write(codecs.BOM_UTF8)
    targetw = csv.writer(target)
    return targetw


def split_file(fname):
    freader = csv.reader(open(fname, 'r'))
    
    parts = 1
    fwriter = file_writer(fname, parts)

    count = 1
    print 'start part', parts
    for row in freader:
        if count > SIZE:
            parts += 1
            fwriter =  file_writer(fname, parts)
            count = 1
            print 'start part', parts
        fwriter.writerow(row_wrapper(row))
        count += 1
        if not count%500000:
            print 'finished: ', count + (parts-1)*SIZE
    print '========== DONE ==========='
    print 'total parts is', parts
    print 'total records: ', count + (parts-1)*SIZE -1


if __name__ == '__main__':
    split_file(sys.argv[1])
