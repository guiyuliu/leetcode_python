"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同

题解：其实就是一个二叉树的前序遍历，获得一个list，遍历完成之后再按照左空右节点的方式重新排列

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:

        preorder = list()
        def recur(root):
            if root:       
              preorder.append(root)
              recur(root.left)
              recur(root.right)
        # 先进性前序排列
        recur(root)
        # 排列完成后重新变成二叉树
        n = len(preorder)
        for i in range(1, n):
            pre, cur = preorder[i-1], preorder[i]
            pre.left = None
            pre.right = cur
        return 
            
        




