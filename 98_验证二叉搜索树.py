"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

low 和high 初始设定为负无穷和正无穷， 如果left比，hig就是根节点的值
如果跟right比，low 就是根节点的值
最后返回左右节点 and 的值

"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def recur_helper(root, low, high):
            if not root:
                return True
            if root.val <= low or  root.val >= high:
                return False
            l_ret = recur_helper(root.left, low, root.val)
            r_ret = recur_helper(root.right, root.val, high)
            return l_ret and r_ret

        return recur_helper(root, float("-inf"), float("inf"))
