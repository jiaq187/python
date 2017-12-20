#!/usr/bin/env python
# -*- coding:utf-8 -*-
#s = set([1,2,3])
s = set([1,1,2,2,3,3])
print(s)
s.add(4)
print(s)
s.add(6)
print(s)
s.remove(4)
print(s)
s.remove(6)
print(s)
s1 = set([1,2,3])
s2 = set([2,3,4])
s3 = s1 & s2
s4 = s1 | s2
print(s3)
print(s4)
a = ['c','b','a']
a.sort()
print(a)
a = 'abc'
b = a.replace('a','A')
print(b)
print(a)
