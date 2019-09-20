# https://algospot.com/judge/problem/read/ITES

import queue

#선형 합동 난수 생성기
class RNG:
    def __init__(self):
        self.seed = 1983
        self.MOD = 2 ** 32
    def next(self):
        ret = self.seed
        self.seed = (self.seed * 214013 + 2531011) % self.MOD
        return ret % 10000 + 1

#온라인 알고리즘
def countRanges(k, n):
    rng = RNG() #신호값을 생성하는 난수 생성기
    signalQueue = queue.Queue()  #현재 구간에 들어 있는 숫자들을 저장하는 큐
    ret, rangeSum = 0, 0
    for i in range(n):
        #구간에 숫자를 추가한다.
        newSignal = rng.next()
        rangeSum += newSignal
        signalQueue.put(newSignal)

        #구간의 합이 k를 초과하는 동안 구간에서 숫자를 뺀다.
        while rangeSum > k:
            rangeSum -= signalQueue.get()

        if rangeSum == k: ret += 1

    return ret

print(countRanges(8791, 20))
print(countRanges(5265, 5000))
