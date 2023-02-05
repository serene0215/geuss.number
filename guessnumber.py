import random
r = random.randint(1, 100)
count = 0
while True:
    count = count + 1
    number = input('請輸入數字：')
    if int(number) == r:
        print('終於猜對了')
        print('這是你猜的第',count , '次')    
        break
    elif int(number) > r:    
        print('猜錯了！你猜的比答案大')
    elif int(number) < r:
        print('猜錯了！你猜的比答案小')
    print('這是你猜的第',count , '次')    
