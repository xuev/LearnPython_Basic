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
    print("-" * 50)
    val = input("请输入带温度标识符号的温度值（例如：24C 或 100F）： ")
    if len(val) != 0:
        if val[-1] in ['C', 'c']:
            for m in val[0:-1]:
                if m in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                    f = 1.8 * float(val[0:-1]) + 32
                    print()
                    print("    您输入的是 " + str(float(val[0:-1])) + " °C，转换后的温度为： %0.2f °F" % f)
                    print()
                    return fc(val)
            print()
            print("    输入有误，请重新输入！")
            print()
            return fc(val)
        elif val[-1] in ['F', 'f']:
            for n in val[0:-1]:
                if n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                    c = (float(val[0:-1]) - 32) / 1.8
                    print()
                    print("    您输入的是 " + str(float(val[0:-1])) + " °F，转换后的温度为： %0.2f °C" % c)
                    print()
                    return fc(val)
            print()
            print("    输入有误，请重新输入！")
            print()
            return fc(val)
        elif val in ['quit', 'exit', 'q']:
            return
        else:
            print()
            print("    输入有误，请重新输入！")
            print()
            return fc(val)
    else:
        print()
        print("    输入有误，请重新输入！")
        print()
        return fc(val)

a = fc(input())
