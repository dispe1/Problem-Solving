import sys
from random import Random
class TreapNode:
    def __init__(self, key, value, priority, parent=None, left=None, right=None, size=1):
        self.key = key
        self.value = value
        self.priority = priority
        self.parent = parent
        self.left = left
        self.right = right
        self.size = size

    def __repr__(self):
        return str((self.key, self.value, self.priority))

    def setLeft(self, newLeft):
        self.left = newLeft
        self.calcSize()

    def setRight(self, newRight):
        self.right = newRight
        self.calcSize()

    def calcSize(self):
        self.size = 1
        if self.left: self.size += self.left.size
        if self.right: self.size += self.right.size

    def inorder(self):
        if self.left: self.left.inorder()
        print(self.key)
        if self.right: self.right.inorder()

    #self를 루트로 하는 트립을 key 미만의 값과 이상의 값을 갖는 두 개의 트립으로 분리한다.
    def split(self, key):
        #루트가 key 미만이면 오른쪽 서브트리를 쪼갠다.
        if self.key < key:
            if self.right != None:
                rs = self.right.split(key)
                self.setRight(rs[0])
                return (self, rs[1])
            else:
                return (self, None)
        ##루트가 key 이상이면 왼쪽 서브트리를 쪼갠다.
        ls = self.left.split(key)
        self.setLeft(ls[1])
        return (ls[0], root)

    #self를 루트로 하는 트립에 새 노드 node를 삽입한 뒤 트립의 루트를 반환한다.
    def insert(self, node):
        if self.priority < node.priority:
            splitted = self.split(node.key)
            node.setLeft(splitted[0])
            node.setRight(splitted[1])
            return node
        elif node.key < self.key:
            self.setLeft(self.left.insert(node))
        else:
            if self.right != None:
                self.setRight(self.right.insert(node))
            else:
                self.setRight(node)
        return self

    # max(self) < min(b)일 때 이 둘을 합친다.
    def merge(self, node):
        if not node: return self
        if self.priority < node.priority:
            node.setLeft(self.merge(node.left))
            return node
        if self.right:
            self.setRight(self.right.merge(node))
        else:
            self.setRight(node)
        return self

    #self를 루트로 하는 트립에서 key를 지우고 결과 트립의 루트를 반환한다.
    def erase(self, key):
        if self.key == key:
            return self.left.merge(self.right) if self.left else self.right
        if key < self.key:
            self.setLeft(self.left.erase(key))
        else:
            self.setRight(self.right.erase(key))

        return self

    def kth(self, k):
        #왼쪽 서브트리의 크기를 우선 계산한다.
        leftSize = 0
        if self.left: leftSize = self.left.size
        if k <= leftSize: return self.left.kth(k)
        if k == leftSize + 1: return self
        return self.right.kth(k - leftSize - 1)

    def countLessThan(self, key):
        if self.key >= key:
            return self.left.countLessThan(key) if self.left != None else 0
        ls = self.left.size if self.left != None else 0
        return ls + 1 + self.right.countLessThan(key)


class Treap:
    def __init__(self, seed=0, maxHeapId=sys.maxsize):
        self.random = Random(seed)
        self.maxHeapId = maxHeapId
        self.root = None

    #key, data로 노드를 생성하여 트립에 삽입한다
    def insert(self, key, data=None):
        node = TreapNode(key, data, self.random.randrange(self.maxHeapId))
        if not self.root:
            self.root = node
        else:
            self.root = self.root.insert(node)

    #key를 지움
    def delete(self, key):
        if self.root != None:
            self.root = self.root.erase(key)


    #k번째 원소를 반환 O(lgN)
    def findKth(self, k):
        if k <= 0 or k > self.root.size: return None
        return self.root.kth(k)

    def countLessThan(self, key):
        return self.root.countLessThan(key) if self.root != None else 0

    def inorder(self):
        if self.root:
            self.root.inorder()

    def __repr__(self):
        return str(self.root)

if __name__ == '__main__':
    treap = Treap()
    treap.insert(1)
    treap.insert(2)
    treap.insert(3)
    print(treap, treap.root.left, treap.root.right, treap.root.size)
    treap.delete(2)
    print(treap, treap.root.left, treap.root.right, treap.root.size)
    print(treap.findKth(2), treap.root.size)
    print(treap.countLessThan(2))
