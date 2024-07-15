# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()

        for d in descriptions:
            parent_val = d[0]
            child_val = d[1]
            if parent_val not in node_map:
                parent=TreeNode(parent_val)
                node_map[parent_val] = parent
            if child_val not in node_map:
                child=TreeNode(child_val)
                node_map[child_val] = child
            
            if d[2]==1:
                node_map[parent_val].left = node_map[child_val]
            elif d[2]==0:
                node_map[parent_val].right=node_map[child_val]
            children.add(child_val)
        
        for node in node_map:
            if node not in children:
                return node_map[node]
        return None
        