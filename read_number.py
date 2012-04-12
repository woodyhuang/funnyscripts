#encoding: utf-8

"""Read numbers in Chinese"""

__version__ = '0.1, for fun'
__author__ = 'woody'

import sys

base_pronunce = {
    '1': u'一',
    '2': u'二',
    '3': u'三',
    '4': u'四',
    '5': u'五',
    '6': u'六',
    '7': u'七',
    '8': u'八',
    '9': u'九',
    '0': u'零',
}

advance_pronunce = {
    2: u'十',
    3: u'百',
    4: u'千',
    5: u'万',
    6: u'十',
    7: u'百',
    8: u'千',
    9: u'亿',
    10: u'十',
    11: u'百',
    12: u'千',
    13: u'万',
    14: u'兆',
    15: u'十',
    16: u'百',
    17: u'千',
    18: u'万',
    19: u'十',
    20: u'百',
    21: u'千',
}

MAX_LEN = len(advance_pronunce.keys()) +1

def read_number(num):
    pronunce = []
    for i in range(1, len(num)+1):
        if i == 1:
            if num[-i] != '0' or len(num) == 1:
                pronunce.append(base_pronunce[num[-i]])
            continue

        if num[-i] == '0':
            if num[-i+1] != '0':
                pronunce.append(base_pronunce['0'])
            continue
        
        pronunce.append(advance_pronunce[i])
        pronunce.append(base_pronunce[num[-i]])
            
    return ''.join(pronunce[::-1])


def main():
    if len(sys.argv) < 2:
        print u'''
        你没有输入任何数字。

        用法：python read_number.py 数字1 [数字2 数字3 ...]
        '''
        sys.exit(0)
    
    ns = sys.argv[1:]
    for n in ns:
        if not n.isdigit():
            print u'%s 不是数字' % n
            continue

        n = '%d' % int(n)
        if len(n) > MAX_LEN:
            print u'%s 是%d位数，超过此工具接受最大%d位数，不能读' % (n ,len(n), MAX_LEN)
            continue

        print u'%s 是%d位数，读音是：%s' % (n, len(n), read_number(n))


if __name__ == '__main__':
    main()
