class Solution:
    #def find_left(self,ch,i,c):
    #     for j in range(i-1,-1,-1):
    #         if ch==c[j]:
    #             return j
    #     return -1

    # def find_right(self,ch,i,c):
    #     for j in range(i+1,len(c)):
    #         if ch==c[j]:
    #             return j
    #     return -1



    #def minimumLength(self, s: str) -> int:
    #     c=list(s)
    #     i=1
    #     while i<(len(s)):
    #         ch=c[i]
    #         if ch!='':
    #             l=self.find_left(ch,i,c)
    #             r=self.find_right(ch,i,c)
    #             #print(ch,l,r,i)
    #             if l!=-1 and r!=-1:
    #                 # c.pop(r)
    #                 # c.pop(l)
                    
    #                 # c.insert(l,'')
    #                 # c.insert(r,'')
    #                 c[l]=''
    #                 c[r]=''
                  
    #         i+=1
    #     count=0
    #     for i in range(len(c)):
    #         if c[i]!='':
    #             count+=1
    #     return count
    def minimumLength(self, s: str) -> int:
        char_freq_map=Counter(s)
        print(s)
        delete_count=0
        for f in char_freq_map.values():
            if f%2==1:
                delete_count+=f-1
            else:
                delete_count+=f-2
        return len(s)-delete_count

    