class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            i=0
            while i<len(s):
                #print(s[i:i+len(part)])
                if s[i:i+len(part)]==part:
                    s=s[:i]+s[i+len(part):]
                    #print("Matched",s)
                    i=0
                else:
                    i+=1
        #print(s)
        return s
