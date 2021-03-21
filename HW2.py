# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:08:11 2021

@author: user
"""

"""
使用者輸入一個範圍的整數
    求--> 4的倍數有哪些?
    求-->哪些是質數 (EX:5-> 2,3,4是否整除5)
"""

start = int(input("初始值:"))
end = int(input("終止值:"))
print(list(range(start,end+1)))

for a in range(start,end+1):
    if a % 4 == 0:
        print(a,'是4的倍數')


for n in range(start,end+1):
    for b in range(2,n):
        if n % b == 0:
            break
        elif b == n-1:
            print(n,'是質數')
    if n == 2:
        print(n,'是質數')

        
        
    
