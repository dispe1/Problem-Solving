#공집합 = 0
toppings = 0
#꽉 찬 집합 (ex: 0~19)
fullPizza = (1 << 20) - 1
#원소 추가
p = 2
toppings |= (1 << p)
#print(toppings)
#원소의 포함 여부 확인
if toppings & (1 << p):
    #원소의 삭제
    toppings &= ~(1 << p)
#print(toppings)
#원소의 토글
toppings ^= (1 << p)
#print(toppings)

#두 집합 연산
#added = (a | b)         #합집합
#intersection = (a & b)  #교집합
#removed = (a & ~b)      #차집합
#toggled = (a ^ b)       #하나에만 포함된 원소들의 집합

#짝수 : 0, 홀수 : -1 리턴
def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return(parity)

#print(parityOf(toppings))

#최하위 원소 번호
def lowestSet(int_type):
    low = (int_type & -int_type)
    lowBit = -1
    while (low):
        low >>= 1
        lowBit += 1
    return(lowBit)

#print(lowestSet(toppings))

#최소 원소 찾기
firstTopping = (toppings & -toppings)
#print(firstTopping)
#최소 원소 지우기
toppings &= (toppings -1)
#print(toppings)

#모든 부분 집합 순회하기
subset = toppings
while(subset):
    ###
    subset = ((subset-1) & toppings)

#집합의 크기 구하기
def bitLen(int_type):
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    return(length)
#집합의 크기, 1의 갯수 구하기
def bitLenCount(int_type):
    length = 0
    count = 0
    while (int_type):
        count += (int_type & 1)
        length += 1
        int_type >>= 1
    return(length, count)
#1의 갯수 구하기
def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)
