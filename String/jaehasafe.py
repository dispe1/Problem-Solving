# https://algospot.com/judge/problem/read/JAEHASAFE
from kmpSearch import kmpSearch

def shifts(original, target):
    return kmpSearch(original + original, target)[0]


if __name__ == '__main__':
    input = ['abbab', 'babab', 'ababb', 'bbaba']
    ret = 0
    for i in range(len(input)-1):
        if i % 2 == 0:
            ret += shifts(input[i+1], input[i])
        else:
            ret += shifts(input[i], input[i+1])
    print(ret)
