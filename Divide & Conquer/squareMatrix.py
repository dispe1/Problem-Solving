#n*n 크기의 항등 행렬(identity matrix)을 반환하는 함수
def identity(n):
    return [[1 if i == j else 0 for j in range(n) ] for i in range(n)]

def matrix_multiplication(mat1, mat2):
    matR = [ len(mat2[0])*[0] for i in range (len(mat1)) ]

    for i in range (len(matR) ):
        for j in range ( len(matR[i]) ):
            for k in range ( len(mat1[i] ) ):
                matR[i][j] += mat1[i][k]*mat2[k][j]

    return matR

#A^m을 반환한다.
def pow(A, m):
    #기저 사례 A^0 = I
    if m == 0: return identity(len(A))
    if m % 2 == 1: return matrix_multiplication(pow(A, m - 1), A)
    half = pow(A, m // 2)
    #A^m = (A^(m/2)) * (A^(m/2))
    return matrix_multiplication(half, half)

print (pow([[1, 2], [3, 4]], 2))
