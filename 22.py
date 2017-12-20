#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''def person(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

person('Jack',24,city='Beijing',addr='chaoyang',zipcode=123456)
def person(name,age,*,city='BEijing',job):
    print(name,age,city,job)
person('Jack',24,job='engineer')'''
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
