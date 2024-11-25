class Solution:
    directions={0:[1,3],
        1:[0,2,4],
        2:[1,5],
        3:[0,4],
        4:[1,3,5],
        5:[2,4]}
    

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(s,i,j):
            s=list(s)
            s[i],s[j]=s[j],s[i]
            return ''.join(s)

        visited={}
        b=''.join(str(num)  for row in board for num in row)
        def compare(b,zero_pos,moves):
            if b in visited and visited[b]<=moves:
                return
            visited[b]=moves

            for next_move in self.directions[zero_pos]:
                new_state=swap(b,zero_pos,next_move)
                compare(new_state,next_move,moves+1)

        compare(b,b.index("0"),0)
        return visited.get("123450",-1)


        