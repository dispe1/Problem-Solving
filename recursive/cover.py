# https://algospot.com/judge/problem/read/BOARDCOVER
#주어진 칸을 덮을 수 있는 네가지 방법
#블록을 구성하는 세 칸의 상대적 위치 (dy, dx)의 목록
#(1) ** (2) **  (3) *  (4)  *
#    *       *      **     **
coverType = [[[0, 0], [0, 1], [1, 0]],    #(1)
            [[0, 0], [0, 1], [1, 1]],     #(2)
            [[0, 0], [1, 0], [1, 1]],     #(3)
            [[0, 0], [1, 0], [1, -1]]]    #(4)

#board의 (y, x)를 type번 방법으로 덮거나, 덮었던 블록을 없앤다.
#delta = 1이면 덮고, -1이면 덮었던 블록을 없앤다.
#만약 블록이 제대로 덮이지 않은 경우(게임판 밖으로 나가거나, 겹치거나, 검은칸을 덮을 때)
#False 를 반환한다.
def set(board, y, x, type, delta):
    ok = True
    for i in range(len(coverType[type])):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        board[ny][nx] += delta

        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        elif board[ny][nx] > 1:
            ok = False
    return ok

#board의 모든 빈 칸을 덮을 수 있는 방법의 수를 반환한다.
#board[i][j] = 1 이미 덮인 칸 or 검은 칸
#board[i][j] = 0 아직 덮이지 않은 칸
def cover(board):
    y, x = -1, -1
    #아직 채우지 못한 칸 중 가징 윗줄 왼쪽에 있는 칸을 찾는다.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1: break

    #기저 사례: 모든 칸을 채웠으면 1을 반환한다.
    if y == -1: return 1

    ret = 0
    for type in range (len(coverType)):
        #만약 board[y][x]를 type 형태로 덮을 수 있으면 재귀 호출한다.
        isSet = set(board, y, x, type, 1)
        if isSet:
            ret += cover(board)
        #덮었던 블록을 치운다.
        set(board, y, x, type, -1)

    return ret

board = [[1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1]]
print(cover(board))
