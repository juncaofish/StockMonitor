#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import re
import urllib
import urllib2

def getHtml(URL):
    ''' Get Html page source with URL
    '''
    Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'} 
    req = urllib2.Request(URL, headers = Headers)
    Html=urllib2.urlopen(req).read().decode('gbk')
    return Html