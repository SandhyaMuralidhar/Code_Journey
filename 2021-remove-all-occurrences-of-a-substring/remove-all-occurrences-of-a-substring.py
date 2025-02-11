class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            i=0
            while i<len(s):
                if s[i:i+len(part)]==part:
                    s=s[:i]+s[i+len(part):]
                    i=0
                else:
                    i+=1
        return s
