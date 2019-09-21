#펜윅 트리의 구현. 가상의 배열 A[]의 부분 합을 빠르게 구현할 수 있도록 한다.
#초기화시에는 A[]의 원속 ㅏ전부 0이라고 생각한다.
class FenwickTree:
    def __init__(self, n):
        self.tree = [0 for _ in range(n+1)]

    #A[0:pos+1]의 부분합을 구한다.
    def sum(self, pos):
        #인덱스가 1부터 시작한다고 생각하자.
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.tree[pos]
            #다음 구간을 찾기 위해 최종 비트를 지운다.
            pos &= (pos-1)
        return ret

    #A[pos]에 val을 더한다.
    def add(self, pos, val):
        pos += 1
        while pos < len(self.tree):
            self.tree[pos] += val
            pos += (pos & -pos)
