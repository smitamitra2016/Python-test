'''
Created on 26 Jan 2017

@author: Nomad Digital
'''
file = open('menu.txt')
for idx,line in enumerate(file.readlines()):
    print(idx,line,end='')