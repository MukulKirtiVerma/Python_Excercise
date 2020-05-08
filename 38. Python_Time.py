# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:23:52 2018

@author: sky
"""

import time;  # This is required to include time module.
"""
Getting current time
"""
ticks = time.time()
print ("Number of ticks :", ticks)

"""
Index	Attributes	    Values
0	tm_year	           2008
1	tm_mon	           1 to 12
2	tm_mday	           1 to 31
3	tm_hour	           0 to 23
4	tm_min	            0 to 59
5	tm_sec	            0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	           0 to 6 (0 is Monday)
7	tm_yday	           1 to 366 (Julian day)
8	tm_isdst	         -1, 0, 1, -1 means library determines DST
"""


import time;

localtime = time.asctime( time.localtime(time.time()) )
print ( localtime)


'altzone'
print(time.altzone)
 'asctime',#current date and time
 print(time.asctime())

 'perf_counter',
 print(time.perf_counter())

 'ctime',#current datetime
 print(time.ctime())

 'daylight',#print daylight of day
 print(time.daylight)


 'gmtime',#get detail info of time
 print(time.gmtime())

 'localtime',#get local time detail
 print(time.localtime())


 'monotonic',#give monotonic time
 print(time.monotonic())


 'perf_counter_ns',
 print(time.perf_counter_ns())

 'process_time',
 print(time.)

 'process_time_ns',
 print(time.)

 'sleep',#sleep the exicution for few seconds
 print(time.sleep(10))

 'strftime',#convert to time
 print(time.strftime('6:0'))

 'strptime',
 print(time.strptime('2 3 5 06:09:08 1987'))

 'struct_time',#create time
 print(time.struct_time("0203051987"))

 




#calender

import calendar

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)