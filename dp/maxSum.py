import sys
#최대 연속 부분 구간 합 문제 풀이 동적 계획법
def maxSum(arr):
    n = len(arr)
    ret = -sys.maxsize-1
    psum = 0

    for i in range(n):
        psum = max(psum, 0) + arr[i]
        ret = max(psum, ret)

    return ret

arr = [-7, 4, -3, 6, 3, -8, 3, 4]
print(maxSum(arr))
