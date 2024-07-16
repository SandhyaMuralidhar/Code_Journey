# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out =[]
        def helper(root,out):
            if root is None:
                return
            out.append(root.val)
            helper(root.left,out)
            helper(root.right,out)
        helper(root,out)
        return out



            