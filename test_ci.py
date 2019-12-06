#!/usr/bin/env python
# encoding: utf-8
#@author: 张新礼
#@file: test_ci.py
#@time: 2019/12/6 上午10:08


for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

