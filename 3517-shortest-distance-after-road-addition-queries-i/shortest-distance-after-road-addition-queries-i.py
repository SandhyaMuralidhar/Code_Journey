class Solution:

    def bfs(self, adj_nodes,n):
        visited=[False]*n
        myqueue=deque()
        myqueue.append(0)
        visited[0]=True
        current_layer_node_count=1
        next_layer_node_count=0
        layers_explored=0
        while myqueue:
            for _ in range(current_layer_node_count):
                current_node = myqueue.popleft()
                if current_node==n-1:
                    return layers_explored
                for neighbor in adj_nodes[current_node]:
                    if visited[neighbor]:
                        continue
                    myqueue.append(neighbor)
                    visited[neighbor]=True
                    next_layer_node_count+=1
            current_layer_node_count=next_layer_node_count
            next_layer_node_count=0
            layers_explored+=1
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