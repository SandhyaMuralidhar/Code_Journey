class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # curra,currb,currc=0,0,0
        # ans=""
        # total_iterations=a+b+c

        # for i in range(total_iterations):
        #     if (a>=b and a>=c and curra!=2) or ((currb==2 or currc==2) and a>0):
        #         ans+='a'
        #         a-=1
        #         curra+=1
        #         currb=0
        #         currc=0
        #     elif (b>=a and b>=c and currb!=2) or ((curra==2 or currc==2) and b>0):
        #         ans+='b'
        #         b-=1
        #         currb+=1
        #         curra=0
        #         currc=0
        #     elif (c>=a and c>=b and currc!=2) or ((currb==2 or curra==2) and c>0):
        #         ans+='c'
        #         c-=1
        #         currc+=1
        #         curra=0
        #         currb=0
        # return ans
        pq=[]
        ans=""
        if a>0:
            heapq.heappush(pq, (-a,'a'))
        if b>0:
            heapq.heappush(pq, (-b,'b'))
        if c>0:
            heapq.heappush(pq,(-c,'c'))

        while pq:
            count,char = heapq.heappop(pq)
            count=-count
            if len(ans)>=2 and ans[-1]==char and ans[-2]==char:
                if not pq:
                    break
                tempcount , tempchar = heapq.heappop(pq)
                tempcount = -tempcount
                ans+=tempchar
                if tempcount-1>0:
                    heapq.heappush(pq,(-(tempcount-1),tempchar))
                heapq.heappush(pq,(-count,char))
            else:
                ans+=char
                if count-1>0:
                    heapq.heappush(pq,(-(count-1),char))
        return ans

