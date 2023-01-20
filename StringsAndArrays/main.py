def isPalindrome(keyword):
    keywordLength = len(keyword)
    if keywordLength == 1:
        return True
    for idx in range(0, keywordLength):
        if keyword[idx] != keyword[keywordLength-idx-1]:
            return False
    return True

def isAllCharsUnique(keyword):
    dicto = {}
    for c in keyword:
        if not dicto.get(c):
            dicto[c] = 1
        else:
            return False
    return True


def isAllCharsUnique2(keyword):
    seto = set(c for c in keyword)
    return len(seto) == len(keyword)


def reverseString(keyword):
    if keyword is None:
        return None
    return keyword[::-1]


def isStringAnagram(s1, s2):
    str1Dict = dict()
    str2Dict = dict()

    if s1 == s2 or len(s1) != len(s2):
        return False
    for c in s1:
        if c not in str1Dict:
            str1Dict[c] = 1
        else:
            str1Dict[c] = str1Dict[c] + 1
    for c in s2:
        if c not in str2Dict:
            str2Dict[c] = 1
        else:
            str2Dict[c] = str2Dict[c] + 1
    
    return str1Dict == str2Dict


def replaceSpace(s1):
    s1 = s1.replace(' ', '%20')
    return s1 
def replaceSpace2(s1):
    s1Len = len(s1)
    sTemp = ""
    for i in range(s1Len):
        if s1[i] == ' ':
            sTemp+='%20' 
        else:
            sTemp+=s1[i]
    return sTemp

def main():
    print("Palindrome")
    print(isPalindrome('level'))
    print(isPalindrome('ey edip adanada pide ye'))
    print(isPalindrome('levelx'))
    print(isPalindrome('ey edip adanada pede ye'))

    print("Is all chars unique")
    print(isAllCharsUnique('avbnshjytlm'))
    print(isAllCharsUnique('1234567890pouytrewq2'))
    print(isAllCharsUnique('zxcvbnmlkjhgfdsa'))

    print("Is all chars unique 2")
    print(isAllCharsUnique('zxcvbnmlkjhgfdsa'))
    print(isAllCharsUnique('zxcvbnmlljhgfdsa'))

    print("Reverse a string")
    print(reverseString('qwerty'))
    print(reverseString('1 2 3 f 5 4 3'))

    print("is anagram")
    print(isStringAnagram('qwerty', 'ertywq'))
    print(isStringAnagram('1 2 3 f 5 4 3', '3 2 1 4 3 f 5'))
    print(isStringAnagram('rakı', 'ırak'))
    print(isStringAnagram('gfds', 'dfg'))
    print(isStringAnagram('12345', '54320'))

    print("replace space with '%20' .. ")
    print(replaceSpace('qwer t y'))
    print(replaceSpace('1 2 3 f 5 4 3'))
    print(replaceSpace2('qwer t y'))
    print(replaceSpace2('1 2 3 f 5 4 3'))

if __name__ == '__main__':
    main()