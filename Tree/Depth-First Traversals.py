#   1
#  / \
# 2   3
# / \
# 4  5


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def postorder_traversal(root):
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder:", inorder_traversal(root))     # [4, 2, 5, 1, 3]
print("Preorder:", preorder_traversal(root))   # [1, 2, 4, 5, 3]
print("Postorder:", postorder_traversal(root)) # [4, 5, 2, 3, 1]
