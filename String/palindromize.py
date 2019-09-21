# https://algospot.com/judge/problem/read/PALINDROMIZE
from kmpSearch import getPartialMatch
#팰린드롬 만들기 문제를 해결하는 KMP 알고리즘의 변형
#a의 접미사이면서 b의 접두사인 문자열의 최대 길이를 구한다.
def maxOverlap(a, b):
    n, m = len(a), len(b)
    pi = getPartialMatch(b)
    #begin = matched = 0에서부터 시작하자.
    begin, matched = 0, 0
    while begin < n:
        #만약 a의 해당 글자가 b의 해당 글자와 같다면
        if matched < m and a[begin + matched] == b[matched]:
            matched += 1
            if begin + matched == n:
                return matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return 0

if __name__ == '__main__':
    input = "there"
    print(len(input)*2 - maxOverlap(input, input[::-1]))
