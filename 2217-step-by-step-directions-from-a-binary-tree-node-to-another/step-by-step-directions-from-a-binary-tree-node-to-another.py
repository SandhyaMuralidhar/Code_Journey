# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.val].append((node.left.val, 'L'))
                graph[node.left.val].append((node.val, 'U'))
                queue.append(node.left)
            if node.right:
                graph[node.val].append((node.right.val, 'R'))
                graph[node.right.val].append((node.val, 'U'))
                queue.append(node.right)
        queue = deque([(startValue, '')])
        visited = set()
        visited.add(startValue)
        while queue:
            cur_node, path = queue.popleft()
            for child, direction in graph[cur_node]:
                if child == destValue:
                    return path+direction
                if child not in visited:
                    visited.add(child)
                    queue.append((child, path + direction))
        return ''

