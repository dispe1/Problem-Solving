#직사각형 합집합의 면적을 구하는 unionArea()함수 구현 O(N^2)
#Rectangle = (x1, y1, x2, y2) | x1 < x2, y1 < y2
def unionArea(rects):
    if len(rects) == 0: return 0
    #이벤트 정보: (x 좌표, 왼쪽인가 오른쪽 인가, 사각형의 번호)
    events = []
    ys = []
    #각 사각형을 순회하면서 y 좌표의 모음과 이벤트의 집합을 찾는다.
    for i in range(len(rects)):
        ys.append(rects[i][1])
        ys.append(rects[i][3])
        events.append((rects[i][0], 1, i))
        events.append((rects[i][2], -1, i))

    #y 좌표의 집합을 정렬하고 중복을 제거
    ys = list(set(ys))
    ys.sort()
    #이벤트 목록을 정렬
    events.sort()
    ret = 0
    #count[i] = ys[i]~ys[i+1] 구간에 겹쳐진 사각형의 수
    count = [0 for _ in range(len(ys)-1)]
    for i in range(len(events)):
        x, delta, rectangle = events[i]
        #count[]를 갱신
        y1 = rects[rectangle][1]
        y2 = rects[rectangle][3]
        for j in range(len(ys)):
            if y1 <= ys[j] and ys[j] < y2:
                count[j] += delta
        #cutLength 값을 계산한다.
        cutLength = 0
        for j in range(len(ys)-1):
            if count[j] > 0:
                cutLength += (ys[j+1] - ys[j])
        #다음 이벤트까지의 거리에 cutLength를 곱한 값을 ret에 더한다.
        if i + 1 < len(events):
            ret += cutLength * (events[i+1][0] - x)
    return ret

print(unionArea([(1,1,3,3), (2, 2, 4, 4)]))
