# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:12:25 2021

@author: user
"""
"""
min=1
max=100
ex:ans=61
    guess=71
   顯示:1-70之間
*猜錯5次離開-->已答錯5次
"""
import random
min = 1
max = 100
answer = random.randint(min, max)

k = 0
while True:
    guess = input('密碼介於 ' + str(min) + '-' + str(max) + ':\n>>')
 
    #檢查輸入的內容是否為數字
    try:
        guess = int(guess)  #把字串轉換成整數
    except ValueError:  #轉換失敗便要求重新輸入數字
        print('格式錯誤，請輸入數字\n')
        continue
 
    #檢查輸入的數字是否介於規定範圍內
    if guess <= min or guess >= max:
        print('請輸入 ' + str(min) + '-' + str(max) + ' 之間的整數\n')
        continue
    k += 1
    if k == 5:
        print('已猜錯5次')
        break
    if guess == answer:
        print('答對了！')
        break
    elif guess < answer:
        min = guess
    else:
        max = guess
