# https://algospot.com/judge/problem/read/PICNIC
n = 4
areFriends = [[True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True]]
taken = [False, False, False, False]
#taken[i] = i번째 학생이 짝을 이미 찾았으면 true, 아니면 false
def countPairings(taken):
    firstFree = -1

    for i in range(n):
        if not taken[i]:
            firstFree = i
            break

    #기저 사례: 모든 학생이 짝을 찾았으면 한가지 방법을 찾았으니 종료
    if firstFree == -1:
        return 1

    ret = 0
    #이 학생과 짝지을 학생을 결정
    for pairWith in range(firstFree+1, n):
        if not taken[pairWith] and areFriends[firstFree][pairWith]:
            taken[firstFree] = taken[pairWith] = True
            ret += countPairings(taken)
            taken[firstFree] = taken[pairWith] = False

    return ret

print(countPairings(taken))
