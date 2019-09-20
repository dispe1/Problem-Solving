# https://algospot.com/judge/problem/read/FENCE

#각 판자의 높이를 저장하는 배열
h = [7, 1, 5, 9, 6, 7, 3]
#스택을 활용한 O(n) 해법
def solveStack():
    #남아 있는 판자들의 위치를 저장한다.
    remaining = []
    ret = 0
    for i in range(len(h)):
        #남아 있는 판자들 중 오른쪽 끝 판자가 h[i]보다 높다면
        #이 판자의 최대 사각형은 i에서 끝난다.
        while(remaining and h[remaining[-1]] >= h[i]):
            j = remaining.pop()
            width = -1
            #j번째 판자 왼쪽에 판자가 하나도 안 남아 있는 경우 left[j] = -1,
            #아닌 경우 left[j] = 남아 있는 판자 중 가장 오른쪽에 있는 판자의 번호가 된다
            if not remaining:
                width = i
            else:
                width = (i - remaining[-1] - 1)
            ret = max(ret, h[j] * width)
        remaining.append(i)
    return ret

print(solveStack())
