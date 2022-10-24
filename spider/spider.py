# -*- coding: utf-8 -*-
'''
@Time    : 2022-10-24 23:54
@Author  : allen
@File    : spider.py

'''

import bs4      # 网页解析，获取数据
import re     # 正则表达式，进行文字匹配
import urllib.request, urllib.error     # 指定url，获取网页数据
import xlwt     # 进行excel操作
import sqlite3  # 进行SQLLite数据库操作