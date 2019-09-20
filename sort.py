def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i

        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j

        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr

def insertionSort(arr):
    for i in range(len(arr)):
        #arr[0:i-1]은 이미 정렬됨
        #arr[0:i-1]에 arr[i]를 끼워 넣음
        j = i

        while j > 0 and arr[j-1] > arr[j]:
            #arr[j+1:i]의 모든 원소는 arr[j]보다 큼
            #arr[0:i] 구간은 arr[j]를 제외하면 정렬되어 있음
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

arr = [4, 3, 2, 1]

print(selectionSort(arr))
print(insertionSort(arr))
