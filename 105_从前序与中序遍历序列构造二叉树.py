"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal

"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 思路：preorder[0]是根节点
        # 题目preorder 和 inorder 均 无重复 元素
        # 在inorder中找到root的index，root_index之前是左子树，后面是右子树，确定左子树长度l1
        # 用哈希表来快速地定位根节点
        # preorder[1: l1] 是左子树，preorder[l1:]是右子树，然后每一层确定一个根节点，
        # 递归地进行左右子树
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root = TreeNode(preorder[pre_left])
            in_root_index = index[preorder[pre_left]]
            left_size = in_root_index - in_left
            # 主要是输入不好确定
            root.left = build(pre_left+1, pre_left+left_size, in_left, in_root_index -1)
            root.right= build(pre_left+left_size+1, pre_right, in_root_index+1, in_right)

            return root
        n = len(preorder)
        index ={element: i for i, element in enumerate(inorder)}
        return build(0, n-1, 0, n-1)
