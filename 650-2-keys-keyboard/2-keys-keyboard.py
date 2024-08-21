class Solution:
    def __init__(self):
        self.n=0

    def min_steps_helper(self, curr_len, paste_len):
        if curr_len==self.n:
            return 0
        if curr_len>self.n:
            return 1000
        opt1 = 2 + self.min_steps_helper(curr_len*2,curr_len)
        opt2 = 1 + self.min_steps_helper(curr_len+paste_len,paste_len)

        return min(opt1,opt2)

    def minSteps(self, n: int) -> int:

        if n==1:
            return 0
        self.n=n
        return 1+self.min_steps_helper(1,1)
        # dp = [1000] * (n + 1)

        # # Base case
        # dp[1] = 0
        # for i in range(2, n + 1):
        #     for j in range(1, i // 2 + 1):
        #         # Copy All and Paste (i-j) / j times
        #         # for all valid j's
        #         if i % j == 0:
        #             dp[i] = min(dp[i], dp[j] + i // j)

        # return dp[n]