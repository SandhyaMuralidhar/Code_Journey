class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        k=0
        out=[]
        while i<len(s):
            
            if k<len(spaces) and i==spaces[k]:
                out.append(' ')
                k+=1
            else:
                out.append(s[i])
                i+=1
        
        return ''.join(out)
        