def swap1(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

def swap2(s, i, j):
    return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))

if __name__ == '__main__':
    print(swap1("2134",0,1))
    print(swap2("2134",0,1))
