'''
Created on 26 Jan 2017

@author: Nomad Digital
'''
a,b = 4,1
if (a+b)<2:
    print('Summation {} is less than 2'.format((a+b)))
else:
    print('Summation {} is greater than 2'.format((a+b)))       

print("abc" if (a+b)<2 else "def")  

choices = dict(
    one = 1,
    two = 2,
    three = 3
    )
#print(choices['four'])
print(choices.get('four')) 
        