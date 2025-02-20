class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        val = 2**(len(nums[0]))
        #print(len(nums))
        for i in range(val):
            n=bin(i)[2:].zfill(len(nums[0]))
            if n not in nums:
                return n
