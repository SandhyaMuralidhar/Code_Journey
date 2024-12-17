class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap=[(-ord(c),count) for c, count in Counter(s).items()]
        heapq.heapify(max_heap)
        res=[]
        while max_heap:
            char, count =heappop(max_heap)
            char = chr(-char)
            cur_taken= min(count, repeatLimit)
            res.append(char*(cur_taken))
            if count-cur_taken>0 and max_heap:
                next_char, next_count = heappop(max_heap)
                next_char=chr(-next_char)
                res.append(next_char)
                if next_count>1:
                    heappush(max_heap,(-ord(next_char),next_count-1))
            
                heappush(max_heap,(-ord(char),count-cur_taken))
        return ''.join(res)


