class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        start=0
        end=0
        num_to_index={}
        sumnumbers=0

        while end<(len(nums)):
            number=nums[end]
            last_occurence=num_to_index.get(number,-1)
            
            while last_occurence>=start or end-start+1>k:
                sumnumbers-=nums[start]
                start+=1
            num_to_index[number]=end
            sumnumbers+=number
            if end-start+1==k:
                ans=max(ans,sumnumbers)
            end+=1
        return ans