'''
Created on 26 Jan 2017

@author: Nomad Digital
'''
try:
    file = open('test.txt')
    for line in file.readlines():
        print(line)
except Exception as e:
    print(e)        