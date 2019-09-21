#H의 부분 문자열로 N이 출현하는 시작 위치들을 모두 반환한다. O(|N|*|H|)
def naiveSearch(H, N):
    ret = []
    #모든 시작 위치를 다 시도해 본다.
    for begin in range(len(H)-len(N)+1):
        matched = True
        for i in range(len(N)):
            if H[begin + i] != N[i]:
                matched = False
                break

        if matched: ret.append(begin)
    return ret


if __name__ == '__main__':
    print(naiveSearch("avava", "ava"))
