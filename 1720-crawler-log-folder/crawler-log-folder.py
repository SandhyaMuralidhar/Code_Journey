class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for s in logs:
            if s == "../":
                count-=1
                if count<0:
                    count=0
            elif s=="./":
                pass
            else:
                count+=1
            
        return count if count>0 else 0
        