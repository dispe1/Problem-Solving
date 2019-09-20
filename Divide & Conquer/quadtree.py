# https://algospot.com/judge/problem/read/QUADTREE

def reverse(it):
    #기저 사례: 첫 글자가 b 또는 w인 경우
    if it[0] == 'b' or it[0] == 'w':
        return it[0]
    idx = 1
    upperLeft = reverse(it[idx:])
    idx += len(upperLeft)
    uppperRight = reverse(it[idx:])
    idx += len(uppperRight)
    lowerLeft = reverse(it[idx:])
    idx += len(lowerLeft)
    lowerRight = reverse(it[idx:])
    #각각 위와 아래 조각들의 위치를 바꾼다.
    return 'x' + lowerLeft + lowerRight + upperLeft + uppperRight

print(reverse('xbwwb'))
print(reverse('xbwxwbbwb'))
print(reverse('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'))
