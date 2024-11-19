class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        start=0
        end=0
        curr_sum=0
        num_to_index={}


        while end<len(nums):
            curr_num = nums[end]
            last_occurence=num_to_index.get(curr_num,-1)
            while last_occurence>=start or end-start+1>k:
                curr_sum-=nums[start]
                start+=1
            curr_sum+=curr_num
            num_to_index[curr_num]=end
            if end-start+1==k:
                ans=max(ans,curr_sum)
            end+=1
        return ans
