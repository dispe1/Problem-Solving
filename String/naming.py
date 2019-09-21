# https://algospot.com/judge/problem/read/NAMING
from kmpSearch import getPartialMatch

#s의 접두사도 되고 접미사도 되는 문자열들의 길이를 반환한다. O(N^(2)lgN)
def getPrefixSuffix(s):
    ret = []
    pi = getPartialMatch(s)
    k = len(s)
    while k > 0:
        #s[:k]는 답이다.
        ret.append(k)
        #s[:k]의 접미사도 되고 접두사도 되는 문자열도 답이다.
        k = pi[k-1]
    return ret

if __name__ == '__main__':
    print(getPrefixSuffix("ababcabababa" + "bcabab"))
