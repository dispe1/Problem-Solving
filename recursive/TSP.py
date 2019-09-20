import sys
n # 도시의 수
dist # 두 도시간의 거리를 저장하는 배열
#path : 지금까지 만든 경로
#visited : 각 도시의 방문 여부
#currentLength: 지금까지 만든 경로의 길이
#나머지 도시들을 모두 방문하는 경로들 중 가장 짧은 것의 길이를 반환한다.
def shortestPath(path, visited, currentLength):
    #기저 사례: 모든 도시를 다 방문했을 때는 시작 도시로 돌아가고 종료한다.
    if len(path) == n:
        return currentLength + dist[path[0]][path[-1]]
    ret = sys.maxsize # 매우 큰 값으로 초기화
    #다음 방문할 도시를 전부 시도해 본다.
    for next in range(n):
        if visited[next]: continue
        here = path[-1]
        path.append(next)
        visited[next] = True
        #나머지 경로를 재귀 호출을 통해 완성하고 가장 짧은 경로의 길이를 얻는다.
        cand = shortestPath(path, visited, currentLength + dist[here][next])
        ret = min(ret, cand)
        path.pop()
    return ret
