class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        out=[False]*len(queries)
        violating_index=[]
        for i in range(1,len(nums)):
            if nums[i]%2==nums[i-1]%2:
                violating_index.append(i)

        for i in range(len(queries)):
            q=queries[i]
            start= q[0]
            end=q[1]
            val=self.binary_search(start+1,end,violating_index)
            if val:
                out[i]=False
            else:
                out[i]=True
        return out
            
    def binary_search(self, start,end,v):
        left=0
        right=len(v)-1
        
        while left<=right:
            mid=left+(right-left)//2
            v_i=v[mid]
            if v_i<start:
                left=mid+1
            elif v_i>end:
                right=mid-1
            else:
                return True
        return False






