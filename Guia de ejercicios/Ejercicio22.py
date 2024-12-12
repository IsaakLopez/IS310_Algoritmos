class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bfs_traversal(root):
    if not root:
        return []

    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Ejemplo de uso
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(bfs_traversal(root))  # Output: [1, 2, 3, 4, 5, 6, 7]
