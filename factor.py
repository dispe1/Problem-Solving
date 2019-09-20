import math
def factor(n): # 소인수 분해
    if n == 1: return [1]
    ret = []
    div = 2

    while n > 1:
        while n % div == 0:
            n /= div
            ret.append(div)
        div += 1

    return ret

print(factor(n))

#에라토스테네스의 체를 수행하면서 소인수분해를 위한 정보도 저장한다.
def eratosthenes2(n, minFactor):
    minFactor[0] = minFactor[1] = -1
    sqrtn = int(math.sqrt(n))

    for i in range(2, sqrtn):
        if minFactor[i] == i:
            for j in range(i*i, n+1, i):
                #아직 약수를 본 적 없는 숫자인 경우 i를 써둔다.
                if minFactor[j] == j:
                    minFactor[j] = i

def factor2(n):
    ret = []
    while n > 1:
        ret.append(minFactor[n])
        n //= minFactor[n]
    return ret


n = 100
minFactor = {i : i for i in range(n+1)}
eratosthenes2(n, minFactor)
print(factor2(n))
