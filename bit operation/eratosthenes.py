import math
#에라토스테네스의 체 구현
n = 100
sieve = [255 for _ in range(len(n+7)//8)]
#k가 소수인지 확인한다.
def isPrime(k):
    return sieve[k >> 3] & (1 << (k & 7))
#k가 소수가 아니라고 표시한다.
def setComposite(k):
    sieve[k >> 3] &= ~(1 << (k & 7))
#이 함수를 사용하고 난 뒤, isPrime()을 이용해 각 수가 소수인지 알 수 있다.
def eratosthenes():
    setComposite(0)
    setComposite(1)
    sqrtn = int(math.sqrt(n))
    for i in range(2, sqrtn+1):
        #이 수가 아직 지워지지 않았다면
        if isPrime(i):
            #i의 배수 j들에 대해 isPrime[j] = False로 둔다.
            #i * i 미만의 배수는 이미 지워졌으므로 신경쓰지 않는다.
            for j in range(i*i, n+1, i):
                setComposite(j)

eratosthenes()
print(isPrime(97))
