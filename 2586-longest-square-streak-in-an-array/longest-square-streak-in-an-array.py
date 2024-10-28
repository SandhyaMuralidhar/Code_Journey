class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        longest_streak=0
        processed_nums=set()
        for n in nums:
            if n in processed_nums:
                continue
            current_length=1
            streak=n
            
            while streak*streak <= 10**5:
                if self._binary_search(nums,streak*streak):
                    streak*=streak
                    current_length+=1
                    processed_nums.add(streak)
                    
                else:
                    break
            longest_streak=max(longest_streak,current_length)
        return longest_streak if longest_streak >=2 else -1


    def _binary_search(self, nums, n):
        left=0
        right=len(nums)-1
        
        while(left<=right):
            mid = left+(right-left)//2
            if nums[mid] == n:
                return True
            elif nums[mid]<n:
                left = mid+1
            elif nums[mid]>n:
                right=mid-1
        return False

                
