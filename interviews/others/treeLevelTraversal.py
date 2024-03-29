class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_traversal(root):
    if not root:
        return None
    
    results = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            results.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return results
