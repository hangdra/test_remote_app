# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : secedule_test.py
@Project  : example
@Time     : 2022/4/26 9:52 上午
@Author   : Liu hang
@Contact_1: 252326397@qq.com
@Contact_2: 
@Software : PyCharm
@License  : (C)Copyright 2021-2028, 
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/4/26 9:52 上午        1.0             None
"""
import schedule
import datetime

def Task3():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print("ok3:",ts)


def Task2():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print("ok2:",ts)

def s_moniter():
    # 清空任务
    schedule.clear()
    # 创建一个按3秒间隔执行任务
    schedule.every(3).seconds.do(Task3)
    # 创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(Task2)
    while True:
        schedule.run_pending()


s_moniter()
