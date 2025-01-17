class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # if len(derived)==1:
        #     if derived[0]==0:
        #         return True
        #     else:
        #         return False
        # i=1
        # original=[]
        # if derived[0]==1:
        #     original.append(0)
        #     original.append(1)
        # else:
        #     original.append(1)
        #     original.append(1)
        # while i<len(derived)-1:
        #     if derived[i]==1 and original[-1]==0:
        #         original.append(1)
        #     elif derived[i]==1 and original[-1]==1:
        #         original.append(0)
        #     i+=1
            
        # #print(original)
        # return original[0]^original[-1]==derived[-1]
            
        orig=[0]
        for i in range(len(derived)-1):
            orig.append(orig[i]^derived[i])
        #print(orig)

        return orig[0]^orig[-1]==derived[-1]