def rotated(array_2d):
    listOfTuples = zip(*array_2d[::-1])
    return [list(elem) for elem in listOfTuples]


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotated(a))
