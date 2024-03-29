class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


def pre_order_traversal(root):
    if root is None:
        return []
    
    results = [root.value]
    results += pre_order_traversal(root.left)
    results += pre_order_traversal(root.right)

    return results
