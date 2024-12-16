class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # while k>0:
            
        #     min_ele=min(nums)
        #     ind=nums.index(min_ele)
        #     nums[ind]=nums[ind]*multiplier
            
            
        #     k-=1
        # return nums
        for _ in range(k):
            min_element=0
            for i in range(len(nums)):
                if nums[i] < nums[min_element]:
                    min_element=i
            nums[min_element]*=multiplier
        return nums
