# https://algospot.com/judge/problem/read/CLOCKSYNC
import sys
SWITCHES = 10
CLOCKS = 16
#LINKED[i] : i번 스위치와 연결된 시계들
LINKED = [[0, 1, 2],
        [3, 7, 9, 11],
        [4, 10, 14, 15],
        [0, 4, 5, 6, 7],
        [6, 7, 8, 10, 12],
        [0, 2, 14, 15],
        [3, 14, 15],
        [4, 5, 7, 14, 15],
        [1, 2, 3, 4, 5],
        [3, 4, 5, 9, 13]]

#모든 시계가 12시를 가리키고 있는지 확인한다.
def areAligned(clocks):
    for c in clocks:
        if c != 12:
            return False
    return True

#switch 스위치를 누른다.
def push(clocks, switch):
    for clock in LINKED[switch]:
        clocks[clock] += 3
        if clocks[clock] == 15: clocks[clock] = 3

#clocks: 현재 시계들의 상태
#switch: 이벤에 누를 스위치의 번호
#가 주어질 때, 남은 스위치들을 눌러서 clocks를 12시로 맞출 수 있는 최소 횟수를 반환한다.
#만약 불가능하다면 sys.maxsize를 반환한다. 경우의 수 :4^10 = 1048576개
def solve(clocks, switch):
    if switch == SWITCHES: return 0 if areAligned(clocks) else sys.maxsize
    #이 스위치를 0번 누르는 경우부터 세 번 누르는 경우까지를 모두 시도한다.
    ret = sys.maxsize
    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, switch + 1))
        push(clocks, switch)

    return ret

clocks = [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12 ]
print(solve(clocks, 0))
