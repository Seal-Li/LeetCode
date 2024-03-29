class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inversed_binary_tree(root):
    if root is None:
        return None
    
    root.left, root.right = inversed_binary_tree(root.right), inversed_binary_tree(root.left)
    return root
