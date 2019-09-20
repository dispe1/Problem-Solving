# https://algospot.com/judge/problem/read/CHRISTMAS

#두 함수의 시간 복잡도는 모두 O(N+K)

#psum[i] = sum(arr[0:i+1]) % k
#D[]의 부분 합 배열 psum[]과 k가 주어질 때, 몇 가지 방법으로 살 수 있는지 반환한다.
#psum[]의 첫 번째 원소 전에 0을 삽입했다고 가정한다.
def waysTobue(psum, k):
    MOD = 20091101
    ret = 0
    #psum[]의 각 값을 몇 번이나 본적 있는지 기록한다.
    count = [0 for _ in range(k)]:
    for i in range(len(psum)):
        count[psum[i]] += 1
    #두 번 이상 본 적 있다면 이 값 중 두 개를 선택하는 방법의 수를 더한다.
    for i in range(k):
        if count[i] >= 2:
            ret = ret +  ( (count[i] * (count[i]-1)) // 2  ) % MOD
    return ret

#ret[i] = max(ret[i-1], ret[prev[psum[i]]] + 1) (prev[psum[i]] != -1)
#D[]의 부분 합 배열 psum[]과 k가 주어질 때, 겹치지 않게 몇 번이나 살 수 있는지 반환한다.
#psum[]의 첫 번째 원소 전에 0을 삽입했다고 가정한다.
def maxBuys(psum, k):
    #ret[i] = 첫 번째 상자부터 i번째 상자까지 고려했을 때 살 수 있는 최대 횟수
    ret = [0 for _ in range(len(psum))]
    #prev[s] = psum[]이 s였던 마지막 위치
    prev = [-1 for _ in range(k)]
    for i in range(len(psum)):
        #i번째 상자를 아예 고려하지 않는 경우
        if i > 0:
            ret[i] =  ret[i-1]
        else:
            ret[i] = 0
        #psum[i]를 전에도 본 적이 있으면, prev[psum[i]]+1부터 여기까지 쭉 사본다.
        loc = prev[psum[i]]
        if loc != -1: ret[i] = max(ret[i], ret[loc]+1)
        #prev[]에 현재 위치를 기록한다.
        prev[psum[i]] = i
    return ret[-1]
