class Solution:
    def getLucky(self, s: str, k: int) -> int:
        out=''
        for c in s:
            #print(c,ord(c))
            out +=str(ord(c)-ord('a')+1)
       

        out = int(out)
        num = out
        ans=0
        for i in range(k):
            ans=0
            while num>0:
                rem = num%10
                ans= ans+rem
                num=num//10
                print(ans)
            num=ans
        #print(ans)
        return ans