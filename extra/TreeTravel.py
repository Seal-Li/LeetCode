class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_travel(root):
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


def pre_order_travel(root):
    if root is None:
        return []
    
    # 访问根节点的值
    results = [root.value]
    # 递归遍历左子树
    results += pre_order_travel(root.left)
    # 递归遍历右子树
    results += pre_order_travel(root.right)
    
    return results


def in_order_travel(root):
    if root is None:
        return []
    
    # 递归遍历左子树
    results = pre_order_travel(root.left)
    # 访问根节点的值
    results += [root.value]
    # 递归遍历右子树
    results += pre_order_travel(root.right)
    
    return results


def after_order_travel(root):
    if root is None:
        return []
    
    # 递归遍历左子树
    results = pre_order_travel(root.left)
    # 递归遍历右子树
    results += pre_order_travel(root.right)
    # 访问根节点的值
    results += [root.value]
    
    return results

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print(level_travel(root))
print(pre_order_travel(root))
print(in_order_travel(root))
print(after_order_travel(root))