
# 資料夾管理
import os
import shutil

if os.path.exists('files'):  # 在目前所在的目錄下建立一 files資料夾
    shutil.rmtree('files')   # 如果原目錄有存在 files 資料夾的話，我們先移除掉
os.mkdir('files')            # 新增一個 files 資料夾

n = int(input())

os.chdir('files')            # os.check files 資料夾當中，一個一個生成想產生的資料夾
for i in range(1,n+1):       # 資料夾命名從 f1 開始到 fn
    os.mkdir('f' + str(i))   # 加上型態 string
print(sorted(os.listdir()))  # 完成以後作排序並且列印出來
a = input('Enter')           # 停頓的動作而已，確保第一部分完成

os.rename('f1', 'folder1')   # 更改名稱成 folder1
print(sorted(os.listdir()))
a = input('Enter')

os.rmdir('folder1')          # 刪除名稱為 folder1 的資料夾
print(sorted(os.listdir()))
a = input('Enter')

os.chdir('../')              # 表示在現在的資料夾路徑內
shutil.rmtree('files')       # 刪除整個名為 files 的檔案

