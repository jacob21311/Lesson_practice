
# 字數計算
word = input('請輸入一些文字:\n')
print('你用了 %d 個文字敘述'%(len(word)))

# 對於特定文章搜尋特定字、計算字數與找出出現最多的字(去除標點符號後)

str = '''漢皇重色思傾國，御宇多年求不得。

楊家有女初長成，養在深閏人未識。

天生麗質難自棄，一朝選在君王側。

回眸一笑百媚生，六宮粉黛無顏色。

春寒賜浴華清池，溫泉水滑洗凝脂；

侍兒扶起嬌無力，始是新承恩澤時。

雲鬢花顏金步搖，芙蓉帳暖度春宵；

春宵苦短日高起，從此君王不早朝。

承歡侍宴無閑暇，春從春遊夜專夜。

後宮佳麗三千人，三千寵愛在一身。

金屋妝成嬌侍夜，玉樓宴罷醉和春。

姊妹弟兄皆列士，可憐光彩生門戶。

遂令天下父母心，不重生男重生女。

驪宮高處入青雲，仙樂風飄處處聞。

緩歌慢舞凝絲竹，盡日君王看不足。

漁陽鼙鼓動地來，驚破霓裳羽衣曲。

九重城闕煙塵生，千乘萬騎西南行。

翠華搖搖行復止，西出都門百餘里；

六軍不發無奈何？宛轉蛾眉馬前死。

花鈿委地無人收，翠翹金雀玉搔頭。

君王掩面救不得，回看血淚相和流。

黃埃散漫風蕭索，雲棧縈紆登劍閣。

峨嵋山下少人行，旌旗無光日色薄。

蜀江水碧蜀山青，聖主朝朝暮暮情。

行宮見月傷心色，夜雨聞鈴腸斷聲。

天旋地轉迴龍馭，到此躊躇不能去。

馬嵬坡下泥土中，不見玉顏空死處。

君臣相顧盡霑衣，東望都門信馬歸。

歸來池苑皆依舊，太液芙蓉未央柳；

芙蓉如面柳如眉，對此如何不淚垂？'''
'''
print('------------------------')
string = input('關鍵字:')
str_num = str.count(string)
print('關鍵字的統計字數:', str_num)
print('------------------------')
'''
# 把文字中的標點符號去除
for i in '。，\n ；: ? 「」':
    str = str.replace(i,'')
print('文章總字數:',len(str))

maxstr = ''                # 先假定最多的是空白
maxnumber = 0              # 先假定數量從0開始
for astr in str:           # 一個一個文字來檢視 (文字)
    #print(astr, end='')
    act = str.count(astr)  # 計算次數 (次數)
    if act > maxnumber:    # 透過迴圈重複疊代
        maxstr = astr      # 更新更新
        maxnumber = act    # 更新更新
else:
    print('出現最多的字為:',maxstr,'總共出現幾次:',maxnumber)


