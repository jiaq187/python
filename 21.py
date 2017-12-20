#!/usr/bin/env python
# -*- coding:utf-8 -*-
def persion(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
persion('michale',20)
persion('bob',35,city='beijing')
extra = {'city':'beijing','job':'engineer'}
persion('alex',22,**extra)

