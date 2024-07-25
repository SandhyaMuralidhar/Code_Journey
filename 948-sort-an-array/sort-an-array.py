class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0)+1

        min_val = min(nums)
        max_val = max(nums)

        index = 0
        for val in range(min_val, max_val+1,1):
            while counter.get(val,0)>0:
                nums[index] = val
                index+=1
                counter[val]-=1

        return nums
            