#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author:  xuev (xuewei918@gmail.com)
@Project: LearnPython_Basic
@File: TempConvert.py
@Version: 0.01
@License: MIT Licence
@Create Time: 2017/3/15 02:50
@Description: 
"""


def fc(val):
    val = input("请输入带温度标识符号的温度值（例如：32C）： ")
    if val[-1] in ['C', 'c']:
        f = 1.8 * float(val[0:-1]) + 32
        print("转换后的温度为： %0.2f°F" % f)
        return fc(val)
    elif val[-1] in ['F', 'f']:
        c = (float(val[0:-1]) - 32) / 1.8
        print("转换后的温度为： %0.2f°C" % c)
        return fc(val)
    else:
        print("输入有误，请重新输入！")
        return fc(val)

a = fc(input())
