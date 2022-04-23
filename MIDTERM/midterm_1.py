# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:28:21 2022

@author: marco
"""

L = [1,2,1,2,1,1,3]
x = 1
index_list = []
count = 0

i = 0
while i<len(L):
    if L[i] == x:
        count+=1
        index_list.append(i)
    i+=1
print("Number of occurences = " + str(count))
print(index_list)