class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # s=list(s1)
        # for i in range(len(s1)):
        #     if s1[i]!=s2[i]:
        #         print(s1[i],s2[i])
        #         if s2[i] in s1:
        #             ind=s.index(s2[i],i)
        #             print(s.index(s2[i]))
        #             print(s1[:i]+s2[i]+s1[i+1:ind]+s1[i]+s2[ind+1:])
        #             if s2==s1[:i]+s2[i]+s1[i+1:ind]+s1[i]+s2[ind+1:]:
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             return False
        # return True
        out=[]
        count=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
                out.append(i)
        if count==0 or count==2:
            if count==0:
                return True
            
            if s1==s2[:out[0]]+s2[out[1]]+s2[out[0]+1:out[1]]+s2[out[0]]+s2[out[1]+1:]:
                return True
            else:
                return False
        else:
            return False