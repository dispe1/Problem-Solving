from collections import defaultdict

#접미사 배열을 계산하는 맨버와 마이어스의 알고리즘 O(n(lgn)^2)
def sortBucket(str, bucket, order=1):
    d = defaultdict(list)
    for i in bucket:
        key = str[i:i+order]
        d[key].append(i)
    result = []
    for k,v in sorted(d.items()):
        if len(v) > 1:
            result += sortBucket(str, v, order*2)
        else:
            result.append(v[0])
    return result

def suffixArrayManberMyers(str):
    return sortBucket(str, (i for i in range(len(str))))

if __name__ == "__main__":
        input = 'alohomora'
        arr = suffixArrayManberMyers(input)
        print(arr)
        suf = [input[i:] for i in arr]
        print(suf)
