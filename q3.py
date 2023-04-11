import random
# 猜數字 在 1~100之間的數字請使用者猜測
Max = 100
Min = 0
ans = random.randint(1,99)
count = 0

while True:
    print('請輸入',Min,'<?<',Max,'範圍內的數字:',end='')
    guess = int(input())
    if guess > Min and guess < Max:
        count += 1
        if guess == ans:
            print('Bingo, you are right !')
            break
        elif guess > ans:                # 如果猜測大於(小於)答案，讓猜測值縮減到大於(小於)的數值
            Max = guess
            print("your guess is too big, you've guessing %d times"%(count))
        else:
            Min = guess
            print("your guess is too small, you've guessing %d times"%(count))
    else:
        print('out of range !')








