# https://algospot.com/judge/problem/read/MEASURETIME
from FenwickTree import FenwickTree
#삽입 정렬 시간 재기 문제를 펜윅 트리로 해결하기
def countMoves(A):
    n = len(A)
    tree = FenwickTree(n+1)
    ret = 0
    for i in range(n):
        ret += tree.sum(n) - tree.sum(A[i])
        tree.add(A[i], 1)

    return ret

if __name__ == '__main__':
    input = [5, 1, 4, 3, 2]
    print(countMoves(input))
