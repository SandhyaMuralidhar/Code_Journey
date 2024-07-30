class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = [0]*(len(s))
        count_a = [0]* (len(s))
        n=len(s)
        min_deletions  = float('inf')
        
        counta=0
        countb=0
        out=0
        for i in range(n):
            count_b[i]=countb
            if s[i]=='b':
                countb+=1
        for i in range(n-1,-1,-1):
            count_a[i]=counta
            if s[i]=='a':
                count_b[i]=countb
                counta+=1
            
        
        for i in range(len(s)):
            min_deletions = min(min_deletions, count_a[i]+count_b[i])
    
        return min_deletions