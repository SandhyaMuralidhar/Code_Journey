class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest_streak=0
        s=set(nums)
        for n in nums: 
            current_streak=1
            streak=n
            while streak*streak in s:
                if streak*streak>10**5:
                    break
                streak*=streak
                current_streak+=1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak if longest_streak>=2 else -1


