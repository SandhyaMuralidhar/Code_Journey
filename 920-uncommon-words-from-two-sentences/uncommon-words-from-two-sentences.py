class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        out=[]
        for word in (s1+' '+s2).split(' '):
            d[word]=d.get(word,0)+1
        
        for word in d:
            if d[word]==1:
                out.append(word)
        return out

        