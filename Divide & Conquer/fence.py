# https://algospot.com/judge/problem/read/FENCE

#각 판자의 높이를 저장하는 배열
h = [7, 1, 5, 9, 6, 7, 3]
#h[left:right] 구간에서 찾아낼 수 잇는 가장 큰 사각형의 넓이를 반환한다. O(nlgn)
def solve(left, right):
    #기저 사례: 판자가 하나 밖에 없는 경우
    if left == right: return h[left]
    #[left, mid], [mid+1, right]의 두 구간으로 문제를 분할한다.
    mid = (left + right) // 2
    #분할한 문제를 각개격파
    ret = max(solve(left, mid), solve(mid+1, right))

    #부분 문제 3: 두 부분에 모두 걸치는 사각형 중 가장 큰 것을 찾는다.
    lo, hi = mid, mid+1
    height = min(h[lo], h[hi])
    #[mid, mid+1]만 포함하는 너비 2인 사각형을 고려한다.
    ret = max(ret, height * 2)

    #사각형이 입력 전체를 덮을 때까지 확장해 나간다.
    while left < lo or hi < right:
        #항상 높이가 더 높은 쪽으로 확장한다.
        if hi < right and (lo == left or h[lo-1] < h[hi+1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])

        #확장한 후 사각형의 넓이
        ret = max(ret, height * (hi - lo + 1))

    return ret

print(solve(0, len(h)-1))
