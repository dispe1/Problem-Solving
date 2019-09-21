#접미사 배열을 사용해 원형 문자열 문제를 해결하는 알고리즘의 구현
from suffixArrayManberMyers import suffixArrayManberMyers
#사전순으로 가장 앞에 오는 s의 회전 결과를 구한다. O(n(lgn)^2)
def minShift(s):
    s2 = s + s
    a = suffixArrayManberMyers(s2)
    for i in range(len(a)):
        if a[i] <= len(s):
            return s2[a[i]:a[i]+len(s)]
    #여기로 올 일은 없어야 한다.
    return "__oops__"

if __name__ == "__main__":
    input = "vadakedavraa"
    print(minShift(input))
