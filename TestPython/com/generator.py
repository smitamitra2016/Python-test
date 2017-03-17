'''
Created on 26 Jan 2017

@author: Nomad Digital
'''

def checkEven(n):
    if n%2 == 0:
        return True
    else:
        return False
    

def evenNumberGenerator(n = 2):
    while(n < 100):
        if(checkEven(n)): 
            yield n
        n+=1
    
        
        
for n in evenNumberGenerator():
    print(n)           