# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : example.py.py
@Project  : example
@Time     : 2022/4/6 2:11 上午
@Author   : Liu hang
@Contact_1: 252326397@qq.com
@Contact_2: 
@Software : PyCharm
@License  : (C)Copyright 2021-2028, 
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/4/6 2:11 上午        1.0             None
"""

import asyncio


# async def main():
#     await asyncio.sleep(0.1)

async def main():
    await asyncio.create_task(asyncio.sleep(0.1))


asyncio.run(main())
