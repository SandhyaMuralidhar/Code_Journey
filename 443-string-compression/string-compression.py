class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        out=[]
        k=0
        while i< len(chars):
            c = chars[i]
            j=i+1
            count=1
            while j<len(chars) and chars[i]==chars[j] :
                count+=1
                i+=1
                j+=1
            chars[k]=c
            k+=1
            if count>1 and count<=9:
                chars[k]=str(count)
                k+=1
            elif count>9:
                
                new_count=str(count)
                for ch in new_count:
                    chars[k]=ch
                    k+=1
                
            i+=1

        return k
        