#n : 전체 원소 수
#picked : 지금까지 고른 원소들의 번호
#toPick : 더 고를 원소의 수
#일 때, 앞으로 toPick개의 원소를 고르는 모든 방법을 출력
def pick(n, picked, toPick):
    #기저 사례: 더 고를 원소가 없을 때 고른 원소들을 출력
    if toPick == 0:
        print(picked)
    else:
        #고를 수 있는 가장 작은 번호
        smallest = 0 if not picked else picked[-1] + 1
        #이 단계에서 원소 하나 고름
        for next in range(smallest, n):
            picked.append(next)
            pick(n, picked, toPick-1)
            picked.pop()
n, m = 7, 6
pick(n, [], m)
