class Solution:
    def __init__(self):
        self.n=0

    def min_steps_helper(self,curr_len,paste_len):
        if curr_len == self.n:
            return 0
        if curr_len>self.n:
            return 1000

        opt1=2+ self.min_steps_helper(curr_len*2,curr_len)
        opt2 = 1+ self.min_steps_helper(curr_len+paste_len,paste_len)
        return min(opt1,opt2)

    def minSteps(self, n: int) -> int:
        if n ==1:
            return 0
        self.n = n
        return 1 + self.min_steps_helper(1,1)
        