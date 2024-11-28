class Solution:
    def bfs(self,adj_nodes,n):
        visited=[False]*n
        my_queue=deque()
        my_queue.append(0)
        current_level_total_nodes=1
        next_level_total_nodes=0
        total_levels=0
        visited[0]= True
        while my_queue:
            for _ in range(current_level_total_nodes):
                current_node=my_queue.popleft()
                if current_node==n-1:
                    return total_levels

                for neighbor in adj_nodes[current_node]:
                    if visited[neighbor]:
                        continue
                    my_queue.append(neighbor)
                    visited[neighbor]=True
                    next_level_total_nodes+=1
            current_level_total_nodes=next_level_total_nodes
            next_level_total_nodes =0
            total_levels+=1
        return -1
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_nodes=[[] for _ in range(n)]
        answer=[]
        for i in range(n-1):
            adj_nodes[i].append(i+1)
            
        for q in queries:
            adj_nodes[q[0]].append(q[1])
            answer.append(self.bfs(adj_nodes,n))


        return answer