class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out=[]
        for orgword in words:
            for word in words:
                if orgword!=word and orgword in word and orgword not in out:
                    out.append(orgword)
        return out