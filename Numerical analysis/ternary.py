#삼분 검색, 최대치를 포함하는 후보 구간을 알고 있어야 함.

#우리가 최대치를 찾고 싶어하는 함수
def f(x):
    return -x*x

#[lo, hi] 구간에서 f(x)가 최대치를 갖는 x를 반환한다.
def ternary(lo, hi):
    for iter in range(100):
        a = (2*lo + hi) / 3
        b = (lo + 2*hi) / 3
        if(f(a) > f(b)):
            hi = b
        else:
            lo = a

    return (lo + hi) / 2

print(ternary(-3, 3))
