"""
前序 中序 后序遍历
层序遍历
深度优先遍历： 其实就是前序遍历
"""

preorder = list()
def pre_recur(root):
    if root:    
        preorder.append(root)
        pre_recur(root.left)
        pre_recur(root.right)

midorder = list()
def mid_recur(root):
    if root:
        pre_recur(root.left)
        midorder.append(root)
        pre_recur(root.right)

lastorder =list()
def last_recur(root):
    if root:
        pre_recur(root.left)
        pre_recur(root.right)
        lastorder.append(root)

# 层序优先遍历
level_order = []
def level(root):
    if not root:
        return
    queue = list()
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop()
        level_order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return level_order