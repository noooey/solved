class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_rec(self.root, data)

    def _insert_rec(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert_rec(node.left, data)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert_rec(node.right, data)

    def preOrder(self, node):
        if not node:
            return []
        return [node.data] + self.preOrder(node.right) + self.preOrder(node.left)

    def inOrder(self, node):
        if not node:
            return []
        return self.inOrder(node.right) + self.inOrder(node.left) + [node.data]

    def postOrder(self, node):
        if not node:
            return []
        return self.postOrder(node.right) + [node.data] + self.postOrder(node.left)

    def size(self, node):
        if not node:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def sumOfWeight(self, node):
        if not node:
            return 0
        return node.data + self.sumOfWeight(node.left) + self.sumOfWeight(node.right)

    def maxPathWeight(self, node):
        if not node:
            return 0
        left = self.maxPathWeight(node.left)
        right = self.maxPathWeight(node.right)
        return node.data + max(left, right)

    def mirror(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.mirror(node.left)
            self.mirror(node.right)

    def destruct(self, node):
        if node:
            self.destruct(node.left)
            self.destruct(node.right)
            del node
        self.root = None

t = int(input())
for _ in range(t):
    bst = BinarySearchTree()
    n, *values = map(int, input().split())
    for value in values:
        bst.insert(value)

    print(bst.size(bst.root))
    print(bst.height(bst.root)-1)
    print(bst.sumOfWeight(bst.root))
    print(bst.maxPathWeight(bst.root))
    print(" ".join(map(str, bst.preOrder(bst.root))))
    print(" ".join(map(str, bst.postOrder(bst.root))))
    print(" ".join(map(str, bst.inOrder(bst.root))))
    bst.mirror(bst.root)
    bst.destruct(bst.root)
    if bst.root == None:
        print(0)
    else:
        print(1)
