#!/usr/bin/python
# --*-- coding: UTF-8 --*--

import datetime,time, calendar

now = time.strftime('%Y-%m-%d %H:%M:%S')
print now

now = datetime.datetime.now()
print now

ticks = time.time()
print '当前时间为：', ticks

localtime=time.localtime(time.time())
print '本地时间为：', localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

cal=calendar.month(2016, 1)
print "以下输出2016年1月份的日历："
print cal