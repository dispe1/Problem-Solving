#https://algospot.com/judge/problem/read/NERDS
from vector import vector2
from vector import ccw2
from vector import isInside
from vector import segmentIntersects

#블록 껍질을 찾는 선물 포장 알고리즘의 구현
#points에 있는 점들을 모두 포함하는 최소의 볼록 다각형을 찾는다.
def giftWrap(points):
    n = len(points)
    hull = []
    #가장 왼쪽 아래 점을 찾는다. 이 점은 껍질에 반드시 포함된다.
    pivot = min(points)
    hull.append(pivot)
    while True:
        #ph에서 시작하는 벡터가 가장 왼쪽인 점 next를 찾는다.
        #평행인 점이 여러 개 있으면 가장 먼 것을 선택한다.
        ph = hull[-1]
        next = points[0]

        for i in range(n):
            cross = ccw2(ph, next, points[i])
            dist = (next - ph).norm() - (points[i] - ph).norm()
            if cross > 0 or (cross == 0 and dist < 0):
                next = points[i]
        #시작점으로 돌아왔으면 종료한다.
        if next == pivot: break
        #next를 볼록 껍질에 포함시킨다.
        hull.append(next)
    return hull

#두 블록 다각형의 교차 여부를 확인하는 polygonIntersects() 함수의 구현
#두 다각형이 서로 닿거나 겹치는지 여부를 반환한다.
#한 점이라도 겹친다면 True를 반환한다.
def polygonIntersects(p, q):
    n = len(p)
    m = len(q)
    #우선 한 다각형이 다른 다각형에 포함되어 있는 경우를 확인하자.
    if isInside(p[0], q) or isInside(q[0], p):  return True
    #이 외의 경우, 두 다각형이 서로 겹친다면 서로 닿는 두 변이 반드시 존재한다.
    for i in range(n):
        for j in range(m):
            if segmentIntersects(p[i], p[(i+n)%n], q[j], q[(j+1)%m]):
                return True
    return False

points1 = [vector2(2, 3), vector2(3, 4), vector2(4, 5), vector2(2, 5)]
points2 = [vector2(4, 1), vector2(5, 5), vector2(3, 3), vector2(4, 4)]

polygon1 = giftWrap(points1)
polygon2 = giftWrap(points2)

print(polygonIntersects(polygon1, polygon2))
