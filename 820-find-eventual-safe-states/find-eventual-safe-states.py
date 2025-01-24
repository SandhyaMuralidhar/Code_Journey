class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe={}
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return safe[i]
            safe[i]=True
            return safe[i]

        n=len(graph)
        res=[]

        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

        