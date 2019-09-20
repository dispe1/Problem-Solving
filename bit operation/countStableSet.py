#비트마스크를 이용해 모든 극대 안정 집합의 수를 세는 함수의 구현
n = 4
#explodes[i]는 i와 같이 두었을 때 폭발하는 물질 집합의 비트마스크 표현
explodes = [0b0010, 0b0001, 0b1000, 0b0100]
#주어진 집합이 안정적인지 확인한다.
def isStable(set):
    for i in range(n):
        #집합에 포함된 i번째 원소와 같이 두었을 때 폭발하는 물질이 set에 있다면
        if (set & (1<<i)) and (set & explodes[i]):
            return False
    return True

#모든 극대 안정 집합의 수를 센다
def countStableSet():
    ret = 0
    #모든 집합을 만들어 보자.
    set = 0
    for set in range(1, (1<<n)):
        #우선 안정적이 아니라면 셀 필요가 없다.
        if not isStable(set): continue
        #극대 안정 집합인지 확인하기 위해, 넣을 수 있는 다른 물질이 있나 확인한다.
        canExtend = False
        for add in range(n):
            # add가 집합에 포함되어 있지 않고, set에 add를 넣어도 안정적이라면
            if (set & (1<< add)) == 0 and (explodes[add] & set) == 0:
                canExtend = True
                break
        if not canExtend:
            ret += 1
    return ret

print(countStableSet())
