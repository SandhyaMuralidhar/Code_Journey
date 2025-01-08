class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isprefixsiffix(word1,word2):
            if word2[0:len(word1)]==word1 and word2[-len(word1):]==word1:
                return True
            return False
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isprefixsiffix(words[i],words[j]):
                    count+=1
        return count