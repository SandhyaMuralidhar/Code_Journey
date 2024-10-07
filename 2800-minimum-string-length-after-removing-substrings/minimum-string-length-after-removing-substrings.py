class Solution:
    def minLength(self, s: str) -> int:
        i=0
        while i<len(s):
            print(s[i:i+1])
            if s[i:i+2] == 'AB' or s[i:i+2] == 'CD':
                s=s[:i]+s[i+2:] 
                i=i-1
            else:
                i=i+1
        return len(s)
            

        