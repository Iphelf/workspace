# -*- coding: gbk -*-
# main.py
"""
Created on Tue Jun 21 09:58:59 2016
Author: iphelf
"""

s=list(map(lambda x:x+1,list(range(73))))
t=list(map(lambda x:[x,x,x],list(range(73))))
#filename=raw_input("Enter filename:")
f=open('List.csv','r',encoding= 'utf')
r='start';n=0
while(1):
    r=f.readline()
    if len(str(r))==0:
        break
    print(r,end='')
    t[n]=r.split(',')
    t[n][2]=t[n][2][:-3]
    n+=1
t[0][0]=1


def index(num,mode):
    n=s.index(num)
    if mode == 'G':
        if n%10==0 | 1:
            return 4
        elif n%10==2 | 3 | 4:
            return 3
        elif n%10==5 | 6 | 7:
            return 2
        else:
            return 1
    elif mode == 'p':
        if n<70:
            x=n%10 + 1
        else:
            x=n-64
        y=n/10 + 1
        return [x,y]

def translate(mode):
    if mode=='e':
        return map(lambda x: x[1],t)
    elif mode=='c':
        return map(lambda x: x[2],t)

def printf(list,mode=73):
    if mode == 73:
        for y in range(7):
            for x in range(10):
                print("%2i" %(list[x+y*10]),end=' ')
            print()
        print("%17.2i %2i %2i"%(list[70],list[71],list[72]))

def save(list,mode=73):
    if mode  ==73:
        for y in range(7):
            for x in range(10):
                pass

printf(s)

#printf(translate('c'))
#random.shuffle(s)
#printf(s)
#print index(s[70],'G')
#countfor1=0
#for i in range(100):
#   printf(s)
#   print s.index(03)+1
#   printf(s)
#   if index_G(3) ==1:
#       countfor1+=1