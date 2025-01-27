class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj= defaultdict(list)
        for pre,crs in prerequisites:
            adj[crs].append(pre)
        #print(adj)
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs]=set()
                for neighbour in adj[crs]:
                    prereqMap[crs]|= dfs(neighbour)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        res=[]
        prereqMap={}
        for crs in range(numCourses):
            dfs(crs)
        for u,v in queries:
            res.append(u in prereqMap[v])
        #print(prereqMap)
        return res