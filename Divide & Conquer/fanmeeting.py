# https://algospot.com/judge/problem/read/FANMEETING

#두 긴 자연수의 곱을 반환한다.
#각 배열에는 각 수의 자릿수가 1의 자리에서부터 시작해 저장되어 있다.
#예: multiple([3, 2, 1], [6, 5, 4]) = 123 * 456 = 56088 = [8, 8, 0, 6, 5]
def multiple(a, b):
    c = [0 for _ in range(len(a) + len(b) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += (a[i] * b[j])
    return c

#a += b * (10^k)를 구현한다.
def addTo(a, b, k):
    if len(a) < len(b) + k:
        for i in range(len(b) + k - len(a)):
            a.append(0)

    for i in range(len(b)):
        a[i+k] += b[i]
#a -= b를 구현한다. a >=b 를 가정한다.
def subFrom(a, b):
    for i in range(len(b)):
        a[i] -= b[i]

#두 긴 정수의 곱을 반환한다.
def karatsuba(a, b):
    an, bn = len(a), len(b)
    #a가 b보다 짧을 경우 둘을 바꾼다.
    if an < bn: return karatsuba(b, a)
    #기저 사례: a나 b가 비어 있는 경우
    if an == 0 or bn == 0: return [0]
    #기저 사례: a가 비교적 짧은 경우 O(n^2) 곱셈으로 변경한다.
    if an <= 50: return multiple(a, b)

    half = an // 2
    #a와 b를 밑에서 half자리와 나머지로 분리한다.
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:min(len(b), half)]
    b1 = b[min(len(b), half):]

    #z2 = a1 * b1
    z2 = karatsuba(a1, b1)
    #z0 = a0 * b0
    z0 = karatsuba(a0, b0)
    #a0 = a0 + a1, b0 = b0 + b1
    addTo(a0, a1, 0)
    addTo(b0, b1, 0)
    #z1 = (a0 * b0) - z0 - z2
    z1 = karatsuba(a0, b0)
    subFrom(z1, z0)
    subFrom(z1, z2)
    #ret = z0 + z1 * 10^half + z2 * 10^(half*2)
    ret = z0
    addTo(ret, z1, half)
    addTo(ret, z2, half + half)
    return ret

def hugs(members, fans):
    m, f = len(members), len(fans)
    a = [0 if i == 'F' else 1 for i in members]
    b = [0 if i == 'F' else 1 for i in fans]
    #karatsuba 알고리즘에서 자리 올림은 생략한다.
    c = karatsuba(a,b)
    allHugs = 0
    for i in range(m-1, f):
        if c[i] == 0:
            allHugs += 1
    return allHugs

members = 'FFFMMM'
fans = 'MMMFFF'
print(hugs(members[::-1], fans))

members = 'FFFFF'
fans = 'FFFFFFFFFF'
print(hugs(members[::-1], fans))

members = 'FFFFM'
fans = 'FFFFFMMMMF'
print(hugs(members[::-1], fans))
