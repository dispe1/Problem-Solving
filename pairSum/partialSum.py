#psum[i] = sum(scores[0:i+1])
#sum(scores[a:b]) = psum[b] - psum[a-1]

#주어진 벡터 a의 부분합을 계산한다. O(N)
def partialSum(a):
    ret = [0 for _ in range(len(a))]
    ret[0] = a[0]
    for i in range(1, len(a)):
        ret[i] = ret[i-1] + a[i]
    return ret
#어떤 배열의 부분합 psum[]이 주어질 대, 원래 배열의 a부터 b까지의 합을 구한다. O(1)
def rangeSum(psum, a, b):
    if a == 0: return psum[b]
    return psum[b] - psum[a-1]

#표준편차 = sqrt(분산)
#A[]의 제곱의 부분 합 벡터 sqpsum, A[]의 부분 합 벡터 psum이 주어질 때
#A[a:b+1]의 분산을 반환한다. O(1)
def variance(sqpsum, psum, a, b):
    #우선 해당 구간의 평균을 계산한다.
    mean = rangeSum(psum, a, b) / (b - a + 1)
    ret = rangeSum(sqpsum, a, b) - 2 * mean * rangeSum(psum, a, b) + (b - a + 1) * mean * mean
    return ret

#2차원 psum[y][x] = sum(arr[0:i+1][0:j+1]) O(y*x)
def gridPartialSum(arr):
    ret = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    ret[0] = partialSum(arr[0])
    for y in range(1, len(arr)):
        ret[y][0] = arr[y-1][0] + arr[y][0]
        for x in range(1, len(arr[0])):
            ret[y][x] = ret[y-1][x] + ret[y][x-1] - ret[y-1][x-1] + arr[y][x]
    return ret

#어떤 2차원 배열 A[][]의 부분합 psum[][]이 주어질 때, O(1)
#A[y1][x1]과 A[y2][x2]를 양 끝으로 갖는 부분 배열의 합을 반환한다.
def gridSum(psum, y1, x1, y2, x2):
    ret = psum[y2][x2]
    if y1 > 0: ret -= psum[y1-1][x2]
    if x1 > 0: ret -= psum[y2][x1-1]
    if y1 > 0 and x1 > 0: ret += psum[y1-1][x1-1]
    return ret

#합이 0에 가까운 구간 -> psum 정렬(O(NlogN)) 후 인접한 원소 확인(O(N)) -> O(NlogN)
