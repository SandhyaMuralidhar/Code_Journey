class Solution:
    def tupleSameProduct(self, nums):
        prod_freq={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]*nums[j] in prod_freq:
                    prod_freq[(nums[i]*nums[j])]+=1
                else:
                    prod_freq[(nums[i]*nums[j])]=1
        total_count=0
        for value in prod_freq.values():
            count=(value-1)*value//2
            total_count+=8*count
        return total_count