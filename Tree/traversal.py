# https://algospot.com/judge/problem/read/TRAVERSAL

#트리 순회 순서 변경 문제
#트리의 전위 탐색 결과와 중위탐색 결과가 주어질 때 후위탐색 결과를 출력한다.
def printPostOrder(preorder, inorder):
    #트리에 포함된 노드의 수
    N = len(preorder)
    #기저 사례: 텅 빈 트리면 종료
    if N == 0: return
    #이 트리의 루트는 전위 탐색 결과로부터 곧장 알 수 있다.
    root = preorder[0]
    #이 트리의 왼쪽 서브트리의 크기는 중위 탐색 결과에서 루트의 위치를 찾아서 알 수 있다.
    L = inorder.index(root)
    #오른쪽 서브트리의 크기는 N에서 왼쪽 서브트리와 루트를 뻐면 알 수 있다.
    R = N - 1 - L
    #왼쪽과 오른쪽 서브트리의 순회 결과를 출력
    printPostOrder(preorder[1:L+1], inorder[0:L])
    printPostOrder(preorder[L+1:N], inorder[L+1: N])
    #후위 순회이므로 루트를 가장 마지막에 출력한다.
    print(root)

if __name__ == '__main__':
    preorder = [27, 16, 9, 12, 54, 36, 72]
    inorder = [9, 12, 16, 27, 36, 54, 72]
    printPostOrder(preorder, inorder)
