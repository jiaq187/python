#!/usr/bin/env python
# -*- coding:utf-8 -*-
height = 1.75
weight = 80.5
bmi = weight / height ** 2
print(bmi)
if bmi < 18.5:
    print("过轻")
elif bmi >=18.5 and bmi < 25:
    print("正常")
elif bmi >= 25 and bmi < 28 :
    print("过重")
else:
    print("肥胖")
