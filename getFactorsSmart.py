# https://algospot.com/judge/problem/read/PASS486
import math
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

def getFactorsSamrt(n, minFactor, minFactorPower, factors):
    factors[1] = 1
    for i in range(2, n+1):
        #소수가 아닌 경우, 가장 작은 소인수로 나눈 수(j)의
        #약수의 수를 응용해 i의 약수의 수를 찾는다.
        if minFactor[i] != i:
            p = minFactor[i]
            j = i // p
            #m이 p로 더 나누어지는 경우
            if p == minFactor[j]:
                minFactorPower[i] = minFactorPower[j] + 1

            a = minFactorPower[i]
            factors[i] = (factors[j] // a) * (a+1)

n = 100
minFactor = {i : i for i in range(n+1)}
eratosthenes2(n, minFactor)
minFactorPower = {i : 1 for i in range(n+1)}
factors = {i : 2 for i in range(n+1)}

getFactorsSamrt(n, minFactor, minFactorPower, factors)

print(factors[10])

def getFactorsBrute(n, factors):
    for div in range(1, n+1):
        for multiple in range(div, n+1, div):
            factors[multiple] += 1

n = 100
factors2 = {i : 0 for i in range(n+1)}

getFactorsBrute(n, factors2)
print(factors2[10])
