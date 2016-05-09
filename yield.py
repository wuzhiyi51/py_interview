#!/usr/bin/python
# --*-- coding: UTF-8 --*--

def g(n):
    for i in range(n):
        yield i**2
        
for i in g(5):
    print i,":",
    
print "\n","*"*10,"\n"
def fab(max):
    a,b=0,1
    while a<max:
        yield a
        a, b=b, a+b
        
for i in fab(20):
    print i,",",