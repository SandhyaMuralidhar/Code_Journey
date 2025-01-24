class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dp = {}

        def dfs(node):
            if node in dp: return dp[node]
        
            if len(graph[node]) == 0: return True 
            
            dp[node] = False
            
            for neighbour in graph[node]:
                if not dfs(neighbour): return dp[node]
                
            dp[node] = True
            return dp[node]
                
        res = [i for i in range(len(graph)) if dfs(i)]
        return res 