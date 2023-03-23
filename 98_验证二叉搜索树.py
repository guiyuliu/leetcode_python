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
