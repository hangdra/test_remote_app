# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : p1.py
@Project  : example
@Time     : 2022/4/6 2:00 下午
@Author   : Liu hang
@Contact_1: 252326397@qq.com
@Contact_2: 
@Software : PyCharm
@License  : (C)Copyright 2021-2028, 
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/4/6 2:00 下午        1.0             None
"""
import time
import threading


from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

dt_time = now.strftime("%H:%M:%S")
print("time:", dt_time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

def thread_task():
    time.sleep(1)
    print("thread_task running")
    time.sleep(1)


def main():
    add_t = threading.Thread(target=thread_task)
    add_t.start()
    print(threading.activeCount())
    print(threading.enumerate())
    print(threading.currentThread())
    print(threading.current_thread())
    print("ok2")
    add_t.join()
    print("ok3")


if __name__ == '__main__':
    main()
