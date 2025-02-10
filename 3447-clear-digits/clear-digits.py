class Solution:
    def clearDigits(self, s: str) -> str:
        # s_array=list(s)
        # i=0
        # while i<len(s_array):
        #     if s_array[i].isnumeric():
        #         j=i-1
        #         while(j>=0):
        #             if s_array[j]!="Marked" and s_array[j].isalpha():
        #                 s_array[j]="Marked"
        #                 break
        #             j-=1
        #     i+=1
        #     #print(s_array)
        # out=''
        # i=0
        # while i<len(s):
        #     if s_array[i]!="Marked" and not s_array[i].isnumeric():  
        #         out+=s[i] 
        #     i+=1
        # return out
        l=[]
        i=0
        for i in range(len(s)):
            if s[i].isalpha():
                l.append(s[i])
            else:
                l.pop()
        return ''.join(l)