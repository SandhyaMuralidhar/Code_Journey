class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colours=set()
        balls=set()
        b_c={}
        out=[]
        for q in queries:
            if q[0] not in balls:
                balls.add(q[0])
                colours.add(q[1])
                b_c[q[0]]=q[1]
            else:
                c=q[1]
                b=q[0]
                exist_colour=b_c[b]
                b_c[b]=c
                if exist_colour not in b_c.values():
                    colours.remove(exist_colour)
                colours.add(c)
            out.append(len(colours))
            #print(colours,balls,b_c,out)
        return out