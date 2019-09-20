#https://algospot.com/judge/problem/read/GRADUATION
import sys
from bitOperation import bitCount
n = 4
k = 4
m = 4
l = 4
#prerequisite[i] = i번째 과목의 선수과목의 집합
prerequisite = [0b0000, 0b0001, 0b1011, 0b0000]
#classes[i] = i번째 학기에 개설되는 과목의 집합
classes = [0b1111, 0b1111, 0b1011, 0b1111]
cache = [[-1 for _ in range(1<<n)] for _ in range(m)]

#이번 학기가 semester이고, 지금까지 들은 과목의 집합이 taken일 때
#k개 이상의 과목을 모두 들으려면 몇 학기나 더 있어야 하는가?
#불가능한 경우 sys.maxsize를 반환한다.
def graduate(semester, taken):
    #기저 사례: k개 이상의 과목을 이미 들은 경우
    if bitCount(taken) >= k: return 0
    #기저 사례: m 학기가 전부 지난 경우
    if semester == m: return sys.maxsize
    #메모이제이션
    ret = cache[semester][taken]
    if ret != -1: return ret
    ret = sys.maxsize
    #이번 학기에 들을 수 있는 과목 중 아직 듣지 않은 과목들을 찾는다.
    canTake = (classes[semester] & ~taken)
    #선수 과목을 다 듣지 않은 과목들을 걸러낸다.
    for i in range(n):
        if (canTake & (1<<i)) and ((taken & prerequisite[i]) != prerequisite[i]):
            canTake &= ~(1<<i)
    #이 집합의 모든 부분집합을 순회한다.
    take = canTake
    while(take > 0):
        #한 학기에 l과목까지만 들을 수 있다.
        if bitCount(take) > l: continue
        ret = min(ret, graduate(semester+1, taken | take) + 1)
        take = ((take-1) & canTake)
    #이번 학기에 아무것도 듣지 않을 경우
    ret = min(ret, graduate(semester+1, taken))
    cache[semester][taken] = ret
    return ret

print(graduate(0, 0))
