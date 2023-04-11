
# 回文判斷( is it a palindrome)
def convertInputString():
    # 請使用者輸入一串字串，先轉換字串為統一小寫
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ")
    rawString = rawInput.lower()
    rawList = list(rawString)
    return rawList


def stripAnalphabetics(dirtyList):
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    # 去除相關標點符號
    for character in analphabeticList:
        if character in dirtyList:
            dirtyList.remove(character)
            return stripAnalphabetics(dirtyList)
    return dirtyList


def runPalindromeCheck(straightList):
    reversedList = straightList[::-1]  # 顛倒過來
    if reversedList == straightList:
        return "The text you have entered is a palindrome!"
    else:
        return "The text you have entered is not a palindrome."


def main():
    print("\nPalindrome checker")
    origin = convertInputString()
    origin = stripAnalphabetics(origin)
    palindromeCheck = runPalindromeCheck(origin)
    print(palindromeCheck)


main()