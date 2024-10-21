class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen=set()
        return self.backtrack(seen, s, 0)
    
    def backtrack(self, seen,s,start):
        maxcount=0
        for end in range(start+1,len(s)+1):
            if s[start:end] not in seen:
                seen.add(s[start:end])
                maxcount=max(maxcount,1+self.backtrack(seen,s,end))
                seen.remove(s[start:end])
        return maxcount