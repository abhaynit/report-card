import re

def result(a):
    reg='[a-z A-Z][a-z A-Z 0-9 . _ -]+[@]{1}[a-z A-Z]+[.][a-z A-Z]{,3}'
    return (re.findall(reg,a))


#te = int(input())
te=1 
for i in range(te):
    #sd = input().split()
    sd=["this", "<is_som@radom.stuff>"]
    a=sd[1]
    req='[a-z A-Z]'
    if a[0]=='<' and a[-1]=='>' and len(re.findall(req,a[1])):
        ter = result(a)
        if len(ter)>0 and ter[0][-1]==sd[1][-2]:
            print(sd[0],sd[1])
