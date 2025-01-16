class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = num1
        set_bits= bin(result).count("1")
        total_bits=bin(num2).count("1")
        print(result,set_bits,total_bits)
        current_bit=0
        while set_bits<total_bits:
            if not self.is_set(result,current_bit):
                result=self.set_bit(result,current_bit)
                set_bits+=1
            current_bit+=1

        print(result,set_bits,total_bits)
        while set_bits>total_bits:
            if self.is_set(result,current_bit):
                result=self.unset_bit(result,current_bit)
                set_bits-=1
            current_bit+=1
        return result

    def is_set(self, val,b):
        return val&(1<<b)!=0
    
    def set_bit(self,val,b):
        return val |(1<<b)

    def unset_bit(self,val,b):
        return val & ~(1<<b)




        
    
