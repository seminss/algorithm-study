import sys


class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):
    print(node.item, end='')
    if node.left:
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])


def inorder(node):
    if node.left:
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right:
        inorder(tree[node.right])


def postorder(node):
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    print(node.item, end='')


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tree = {}
    for i in range(n):
        item, left, right = map(str, sys.stdin.readline().split())
        if left == '.':
            left = None
        if right == '.':
            right = None
        tree[item] = Node(item, left, right)
    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
