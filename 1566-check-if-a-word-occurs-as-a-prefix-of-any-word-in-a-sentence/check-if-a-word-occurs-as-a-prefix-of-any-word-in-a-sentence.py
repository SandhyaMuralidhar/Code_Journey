class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i=0
        for word in sentence.split():
            if word.startswith(searchWord):
                return i+1
            i+=1
        return-1