# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
PYTHON PROGRAMME TO VALIDATE THE CREDIT CARD NO  
"""
import re

def result(string):
    lis = ['0000','1111','2222','3333','4444','55555','6666','7777','8888','9999']

    le = len(string)
    reg='\D'
    regex = '[4-6][\d]{15}'
    regex1 = '([4-6][\d]{3})-([\d]{4})-([\d]{4})-([\d]{4})'
    if le==16:
        flag=0
        for i in lis:
            if i in string:
                flag=1
                print("Invalid")
                break
        if flag==0:
            if len((re.findall(regex,string)))>0:
                print("Valid")
            else:
                print("Invalid")
            
            
    elif le==19 :
        flag=0
        str =''.join((re.split(reg,string)))
        for i in range(len(lis)):
            if lis[i] in str:
                flag=1 
                print("Invalid")
                break
        if flag==0:
            if len((re.findall(regex1,string)))>0:
                print("Valid")
            else:
                print("Invalid")
    
    else:
        print("Invalid")

t = int(input())
for i in  range(t):
    print("enter the credit card no : ")
    string=input()
    result(string)
 
