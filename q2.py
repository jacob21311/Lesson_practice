
# 填字遊戲 程式得到文字後可以自行排列，形成一個模板
n = int(input('請輸入執行次數:'))
for i in range(0,n,1):  # 起始值、終止值、變動方向與量
    semester = input('課程期數: ')   # 設立模板的變數
    course = input('課程名稱: ')
    name = input('姓名: ')
    background = input('背景: ')
    expectation = input('期望: ')
print('------------------------')
print('第%s 期 - %s' % (semester, course))           # 將變數代入
print('姓名', name ,',')
print('學生背景:', background)
print('========結訓證明=========')
print('恭喜',name, "修習完課程[",course,']後，')
print('結業獲得:',expectation,'。')
print('Well Done')
print('------------------------')








