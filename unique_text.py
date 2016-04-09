# -*- coding: utf-8 -*-

#A simple script that searches a text file
#unique string and stores them in a text file

import re


with open('anytext.txt') as f:#text file that you want to analyze
        text=f.read()
workfile = open("anytext.txt")

for line in text:
    find=workfile.readline()
    finds=(find[0:60])#select part of the string you are looking for in anytext
    result = re.findall(finds,text)
    u=result.count(finds)
    if u==1:
        s = open('results.txt', 'a')#file in which you want to save the search result
        s.write(str(result)+'\n')
        s.close()
        print (result)
    if u>1:
        pass
        
    
        
        


































