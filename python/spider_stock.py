#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import re
import sys
import urllib
import urllib2
import traceback
from bs4 import BeautifulSoup


def getHtml(URL):
    ''' Get Html page source with URL
    '''
    Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'}
    req = urllib2.Request(URL, headers = Headers)
    Html=urllib2.urlopen(req).read().decode('utf-8')
    return Html


def makeFile(name):
    ''' Make a new folder with timestamp.
    '''
    dateStr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    pathMain = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(pathMain, "data")
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    FilePath = dataDir+'\\%s_%s.txt'%(name,dateStr)
    fhandle = open(FilePath,'w')
    header = u'Date,Open,High,Close,Low,Volume\n'
    fhandle.write(header.encode('utf-8'))
    return fhandle


def logStock(code, dateStart, dateEnd):
    URL = 'http://biz.finance.sina.com.cn/stock/flash_hq/kline_data.php?&symbol=%s&end_date=%s&begin_date=%s&type=plain' %(code, dateEnd, dateStart)
    f = makeFile(code)
    try:        
        html = getHtml(URL)
        f.write(html)        
    except Exception:
        f.write('Error occurs: %s'%traceback.format_exc())
    f.close()
    return html


if __name__ == "__main__":
    ''' This is the main function.
    '''
    code = sys.argv[1]
    dateStart = sys.argv[2]
    dateEnd = sys.argv[3]
    html = logStock(code, dateStart, dateEnd)
    print html
