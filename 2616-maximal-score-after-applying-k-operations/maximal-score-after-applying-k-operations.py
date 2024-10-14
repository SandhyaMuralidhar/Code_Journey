class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)

        ans=0

        while k>0:
            k-=1
            ele=-heapq.heappop(max_heap)
            ans+=ele
            heapq.heappush(max_heap,-(math.ceil(ele/3)))
        
        return ans