class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        processed_num = set()
        current_length=0
        longest_streak=0
        for current in nums:
            if current in processed_num:
                continue    
            current_length=1
            streak=current
            while streak*streak <= 10**5:
                if self._binary_search(nums, streak*streak):
                    streak*=streak
                    current_length+=1
                else:
                    break

            longest_streak = max(longest_streak, current_length)
        return longest_streak if longest_streak>=2 else -1
    
    def _binary_search(self,nums, n):
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=left+(right-left)//2
            if n==nums[mid]:
                return True
            elif n>nums[mid]:
                left=mid+1
            elif n<nums[mid]:
                right=mid-1
            
        return False

        