# https://algospot.com/judge/problem/read/INSERTION
from treap import Treap

#삽입 정렬 뒤집기 문제를 해결하는 알고리즘 O(NlgN)
def solve(n, shifted):
    arr = [0 for _ in range(n)]
    #1~N까지의 숫자를 모두 저장하는 트립을 만든다.
    candidates = Treap()
    for i in range(n):
        candidates.insert(i+1)
    #뒤에서부터 arr[]를 채워나간다.
    for i in range(n-1, -1, -1):
        #후보 중 이 수보다 큰 수가 larger개 있다.
        larger = shifted[i]
        k = candidates.findKth(i + 1 - larger)
        arr[i] = k.key
        candidates.delete(k.key)

    return arr



if __name__ == '__main__':
    n = 5
    input = [0, 1, 1, 2, 3]
    print(solve(n, input))
