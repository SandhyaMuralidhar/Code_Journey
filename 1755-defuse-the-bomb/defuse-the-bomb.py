class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        out=[]
        l=len(code)
        for i in range(l):
            val=0
            if k>0:
               
                for j in range(1,k+1):
                    val+=(code[(i+j)%l])
                    
            elif k<0:
                
                for j in range(1,-(k)+1):
                    val+=(code[(i-j)%l])
            else:
                val =(0)
            
            out.append(val)
        return (out)