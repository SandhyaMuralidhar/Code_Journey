class Solution:
    def compressedString(self, word: str) -> str:
        i=0
        out=''
        while i<len(word):
            j=i+1
            count=1
            char=word[i]
            while j<len(word) and word[i]==word[j] and count<9:
                if word[i]==word[j]:
                    count+=1
                    j+=1
                    i+=1
            i+=1
            out+=''+str(count)+char
        print(out)
        return out

        