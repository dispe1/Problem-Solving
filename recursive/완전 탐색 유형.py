#모든 순열 만들기
def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
        else:  # no break: not found
            return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True

a = [1, 2, 3, 4]
print(next_permutation(a), a)

b = [4, 3, 2, 1]
print(next_permutation(b), b)

#모든 조합 만들기 -> pick.py
#이항 계수 갯수
def bino(n, r):
    #기저 사례: n = r(모든 원소를 다 고르르 경우) 혹은 r = 0(고를 원소가 없는 경우)
    if r == 0 or n == r: return 1
    return bino(n-1, r-1) + bino(n-1, r)
print(bino(7, 6))

cache = {}
def bino2(n, r):
    #기저 사례
    if r == 0 or n == r: return 1
    #계산했던 값이면 곧장 반환
    if (n,r) in cache:
        return cache[(n,r)]
    #직접 계산한 뒤 cache에 저장
    cache[(n, r)] = bino2(n-1, r-1) + bino2(n-1, r)
    return cache[(n,r)]
print(bino2(7, 6))
#2^n가지 경우의 수 만들기
#각 조합을 하나의 n비트 정수로 표현한다고 생각 -> 1차원 for문으로 시도가능
