class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def printData(self):
        print(self.data)
        for i in self.children:
            i.printData()

    def height(self):
        h = 0
        for i in self.children:
            h = max(h, 1 + i.height())
        return h
