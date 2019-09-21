# https://algospot.com/judge/problem/read/HABIT
from countSubStrings import commonPrefix
from suffixArrayManberMyers import suffixArrayManberMyers

#k번이상 출형하는 s의 부분 문자열 중 최대 길이를 찾는다.
def longestFrequent(k, s):
    a = suffixArrayManberMyers(s)
    ret = 0
    for i in range(len(s)-k+1):
        ret = max(ret, commonPrefix(s, a[i], a[i + k -1]))
    return ret

if __name__ == "__main__":
    print(longestFrequent(2,"uhmhellouhmmynameislibe"))
    print(longestFrequent(3, "banana"))
