import random
r = random.randint(1, 100)
while True:
    number = input('請輸入數字：')
    if int(number) == r:
        print('終於猜對了')
        break
    elif int(number) > r:    
        print('猜錯了！你猜的比答案大')
    elif int(number) < r:
        print('猜錯了！你猜的比答案小')    