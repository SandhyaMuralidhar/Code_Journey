class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {}

        for n in nums:
            if n>9:
                MAP_VAL = ''
                for val in str(n):
                    print(val)
                    print(mapping[int(val)])
                    MAP_VAL+=str(mapping[int(val)])
                    d[n] = int(MAP_VAL)
            else:
                
                d[n] =mapping[n]
        
        nums.sort(key = lambda x : (d[x]))
        return nums
                