# https://algospot.com/judge/problem/read/BOGGLE
board = [['U', 'R', 'L', 'P', 'M'],
        ['X', 'P', 'R', 'E', 'T'],
        ['G', 'I', 'A', 'E', 'T'],
        ['X', 'T', 'N', 'Z', 'Y'],
        ['X', 'O', 'Q', 'R', 'S']]
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def inRange(y, x):
    if y < 0 or y >= len(board) or x < 0 or x >= len(board):
        return False
    else:
        return True

def hasWord(y, x, word):
    #기저 사례1: 시작 위치가 범위 밖이면 무조건 실패
    if not inRange(y,x): return False
    #기저 사례2: 첫 글자가 일치하지 않으면 실패
    if board[y][x] != word[0]: return False
    #기저 사례3: 단어 길이가 1이면 성공
    if len(word) == 1: return True
    #인접한 8칸을 검사
    for direction in range(8):
        if hasWord(y + dy[direction], x + dx[direction], word[1:]):
            return True
    return False


word = 'PRETTY'
print(hasWord(1, 1, word))
