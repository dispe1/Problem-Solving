def binarySearch(arr, x): # arr는 오름차순 정렬
    n = len(arr)
    lo, hi = -1, n

    #lo < hi, arr[lo] < x <= arr[hi]
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid
        else:
            hi = mid

    return hi
