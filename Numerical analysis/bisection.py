import math
import sys

def f(x):
    return x * x + 2 * x + 1

#이분법의 예제 구현
def bisection(lo, hi):
    #반복문 불변식을 강제한다.
    if f(lo) > 0:
        lo, hi = hi, lo
    #반복문 불변식 : f(lo) <= 0 < f(hi)
    while: math.fabs(hi - lo) > sys.float_info.epsilon:
        mid = (lo + hi) / 2
        if mid <= 0:
            lo = mid
        else:
            hi = mid
    #가운데 값을 반환한다.
    return (lo + hi) / 2
