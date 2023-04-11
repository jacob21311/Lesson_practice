
# Question 1 來做奇數偶數的判別吧
# 輸入數字後能夠辨別奇偶數外，再把結果回傳給使用者

num = input('請輸入一個數字吧:\n') # input 這個function 就是讓使用者輸入東西
print(type(num)) # 輸出應該會是str(字串)的形式
num = int(num) # 要將 str 轉變成為 int(數字) 的格式
print(type(num))

# 將輸入的數字限制在 1~10 之間
# 輸入正確之後才執行奇偶數分辨
if num >= 1 and num <=10:
    print('正確的範圍 你很棒')
    if num % 2 == 0:
        print('你輸入的是偶數歐歐歐')
    else:
        print('你輸入的是奇數嘿嘿嘿')
else:
    print('不要亂輸入')







