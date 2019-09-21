#접미사 배열을 이용해 다른 부분 문자열의 수를 세는 알고리즘
from suffixArrayManberMyers import suffixArrayManberMyers

#s[i:]와 s[j:]의 공통 접두사의 최대 길이를 계산한다. O(n)
def commonPrefix(s, i, j):
    k = 0
    while i < len(s) and j < len(s) and s[i] == s[j]:
        i += 1
        j += 1
        k += 1
    return k

#s의 서로 다른 부분 문자열의 수를 센다. O(n^2)
def countSubstrings(s):
    a = suffixArrayManberMyers(s)
    ret = 0
    n = len(s)
    for i in range(len(a)):
        cp = 0
        if i > 0: cp = commonPrefix(s, a[i-1], a[i])
        #a[i]의 (n-a[i])개의 접두사들 중에서 cp개는 중복이다.
        ret += (n - a[i] - cp)

    return ret

if __name__ == "__main__":
    input = 'banana'
    print(countSubstrings(input))
