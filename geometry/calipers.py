from vector import vector2
#볼록 다각형의 지름을 재는 회전하는 캘리퍼스 알고리즘
#시계 반대 방향으로 주어진 볼록 다각형에서 가장 먼 꼭지점 쌍 사이의 거리를 반환한다.
def diameter(p):
    n = len(p)
    #우선 가장 왼쪽에 있는 점과 오른쪽에 있는 점을 찾는다.
    left = p.index(min(p))
    right = p.index(max(p))
    #p[left]와 pright]에 각각 수직선을 붙인다. 두 수직선은 서로 반대방향을 가리키므로, A의 방향만을 표현하면 된다.
    calipersA = vector2(0, 1)
    ret = (p[right] - p[left]).norm()
    #toNext[i] = p[i]에서 다음 점까지의 방향을 나타내는 단위 벡터
    toNext = [None for _ in range(n)]
    for i in range(n):
        toNext[i] = (p[(i+1)%n] - p[i]).normalize()
    #a와 b는 각각 두 선분이 어디에 붙은 채로 회전하고 있는지를 나타낸다.
    a, b = left, right
    #반 바퀴 돌아서 두 선분이 서로 위치를 바꿀 때까지 계속한다.
    while a != right or b != left:
        #a에서 다음 점까지의 각도와 b에서 다음 점까지의 각도 중 어느 쪽이 작은지 확인
        cosThetaA = calipersA.dot(toNext[a])
        cosThetaB = -calipersA.dot(toNext[b])
        if cosThetaA > cosThetaB:   # thetaA < thetaB
            calipersA = toNext[a]
            a = (a+1) % n
        else:
            calipersA = toNext[b] * -1
            b = (b+1) % n

        ret = max(ret, (p[a] - p[b]).norm())

    return ret

polygon = [vector2(1,1), vector2(2, 1), vector2(2, 2), vector2(1, 2)]

print(diameter(polygon))
