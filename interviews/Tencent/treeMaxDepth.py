class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # 返回左右子树中较大深度加上当前节点的深度（加 1）
    return max(left_depth, right_depth) + 1

# 示例用法
# 构建一个二叉树
"""
        3
       / \
      9  20
        /  \
       15   7
"""
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 计算二叉树的高度
print("二叉树的高度为:", max_depth(root))  # 输出 3
