
# 及格名單 (pass list)
# 使用集合功能來完成各科級名單的判斷

# 數學及格的所有人
math = {'柯南', '灰原', '步美', '美環', '光彥'}  # 以集合方式存成變數
english = {'柯南', '灰原', '丸尾', '野口', '步美'}

# 找出交集的部分
a = math.intersection(english)
print(a)
print(type(a))  # dictionary 的形式
a1 = list(a)    # list 的形式
a1.sort()       # 不需要返回原列表的方式，去作排序
print(a1)

# 差集的部分
# 數學及格但英文不及格者
b = math.difference(english)
b1 = list(b)
b1.sort()
print(b1)

# 英文及格但數學不及格者
c = english.difference(math)
c1 = list(c)
c1.sort()
print(c1)

# 全班
full = math.union(english) # 聯集
d1 = list(full)
d1.sort()
print(d1)


