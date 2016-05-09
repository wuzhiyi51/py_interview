#!/usr/bin/python
# --*-- coding: UTF-8 --*--

ids=[1,2,3,3,4,2,3,4,5,7,6,1]

news_id=[]

for id in ids:
    if id not in news_id:
        news_id.append(id)
        
print news_id