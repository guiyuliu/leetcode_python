"""
给定一个二叉搜索树 root (BST)，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。

提醒一下， 二叉搜索树 满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。


链接：https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree

"""

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #因为二叉搜索树 右子树所有的和都比根节点大
        # 每个节点变成右子树及其自身的值的和, 其实就是反过来的中序遍历，然后值为右子树的累加
        def dfs(node):
            nonlocal total
            if node:
                dfs(node.right)
                total += node.val
                node.val = total
                dfs(node.left)
            return
        total = 0
        dfs(root)
        return root
