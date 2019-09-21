#커누스-모리스-프랫(Knuth-Morris-Pratt) 문자열 검색 알고리즘

#N에서 자기 자신을 찾으면서 나타나는 부분 일치를 이용해 pi[]를 계산한다. O(|N|)
#pi[i] = N[0:i+1]의 접미사도 되고 접두사도 되는 문자열의 최대 길이
def getPartialMatch(N):
    m = len(N)
    pi = [0 for _ in range(m)]
    #KMP로 자기 자신을 찾는다.
    #N을 N에서 찾는다. begin = 0이면 자기 자신을 찾아버리니까 안됨!
    begin, matched = 1, 0
    #비교할 문자가 N의 끝에 도달할 때까지 찾으면서 부분 일치를 모두 기록한다.
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return pi

#H의 부분 문자열로 N이 출현하는 시작 위치들을 모두 반환한다. O(|H|)
def kmpSearch(H, N):
    n, m = len(H), len(N)
    ret = []
    #pi[i] = N[0:i+1]의 접미사도 되고 접두사도 되는 문자열의 최대 길이
    pi = getPartialMatch(N)
    #begin = matched = 0에서부터 시작하자.
    begin, matched = 0, 0
    while begin <= n-m:
        #만약 H의 해당 글자가 N의 해당글자와 같다면
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
            #결과적으로 m글자가 모두 일치했다면 답에 추가한다.
            if matched ==m: ret.append(begin)
        else:
            #예외: matched가 0인 경우에는 다음 칸에서부터 계속
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                #begin을 옮겼다고 처음부터 다시 비교할 필요가 없다.
                #옮기 후에도 pi[matched-1]만큼은 항상 일치하기 때문이다.
                matched = pi[matched-1]

    return ret

def kmpSearch2(H, N):
    n, m = len(H), len(N)
    ret = []
    pi = getPartialMatch(N)
    #현재 대응된 글자의 수
    matched = 0
    #H의 각 글자를 순회한다.
    for i in range(n):
        #matched번 글자와 H의 해당 글자가 불일치할 경우
        #현재 대응된 글자의 수를 pi[matched-1]로 줄인다.
        while matched > 0 and H[i] != N[matched]:
            matched = pi[matched-1]
        #글자가 대응될 경우
        if H[i] == N[matched]:
            matched += 1
            if matched == m:
                ret.append(i - m + 1)
                matched = pi[matched-1]
    return ret

if __name__ == '__main__':
    print(kmpSearch("avava", "ava"))
    print(kmpSearch2("avava", "ava"))
