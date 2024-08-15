class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {}
        for n in bills:
            d[n]=d.get(n,0)+1
            if n>5:
                remainder = n-5
                if remainder ==5 and d.get(5,0)>0:
                    d[5]-=1
                elif remainder==15 and d.get(10,0)>=1 and d.get(5,0)>=1:
                    d[10]-=1
                    d[5]-=1
                elif remainder==15 and d.get(5,0)>=3:
                    d[5]-=3
                else:
                    return False
                

        
        return True

        