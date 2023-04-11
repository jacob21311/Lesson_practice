
# 查詢路徑下的所有檔案
# 自動抓取路徑下所有檔案的名稱
import os

# 請使用者輸入或指定要查詢的路徑
yourPath = input()
# 列出指定路徑底下所有的檔案(包含資料夾)
allFileList = os.listdir(yourPath)
ID = []           # 新增成正列型態

# 逐一查詢檔案清單
for file in allFileList: # 使用isdir檢查是否為目錄
    if os.path.isdir(os.path.join(yourPath,file)): #   使用join的方式把 '路徑' 與 '檔案名稱' 串起來(等同filePath+fileName)
        print(' I am a directory:' + file)
    # 使用 isfile 判斷是否為檔案
    elif os.path.isfile(os.path.join(yourPath,file)):
        print(' I am a File:' + file)
    # 把 file當中的學號抓出來，另存成一個新的csv檔
        ID.append(file[file.index('_')+1:file.index('.')])
print(ID)







