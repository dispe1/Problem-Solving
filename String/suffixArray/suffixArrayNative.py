#접미사 배열을 계산하는 단순한 알고리즘의

#s의 접미사 배열을 계산한다.
def getSuffixArrayNaive(s):
    #접미사 시작 위치를 담은 배열을 만든다.
    perm = [i for i in range(len(s))]
    #접미사를 비교하는 비교자를 이용해 정렬하면 완성
    perm.sort(key = lambda i: s[i:])
    return perm

if __name__ == '__main__':
    input = 'alohomora'
    arr = getSuffixArrayNaive(input)
    print(arr)
    suf = [input[i:] for i in arr]
    print(suf)
