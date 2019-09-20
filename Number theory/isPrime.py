import math

def eratosthenes(n, isPrime):
    isPrime[0] = isPrime[1] = False
    sqrtn = int(math.sqrt(n))

    for i in range(2, sqrtn):
        #이 수가 아직 지워지지 않았다면
        if isPrime[i]:
            #i의 배수 j 들에 대해 isPrime[j] = False로 둔다.
            #i*i 미만의 배수는 이미 지워졌으므로 신경쓰지 않는다.
            for j in range(i*i, n+1, i):
                isPrime[j] = False

n = 100
isPrime = {i : True for i in range(n+1)}

eratosthenes(n, isPrime)
print(isPrime)
print(isPrime[97])
