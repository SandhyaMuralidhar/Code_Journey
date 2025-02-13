class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # element1=(min(nums))
        # nums.remove(min(nums))
        # count=0
        # while element1<k:
        #     count+=1
        #     element2=(min(nums))
        #     nums.remove(min(nums))
        #     nums.append((element1*2)+element2)
        #     element1=(min(nums))
        #     nums.remove(min(nums))
        # return count
        # nums.sort()
        # count=0
        # while nums[0]<k:
        #     num1=nums[0]
        #     num2=nums[1]
        #     nums.pop(0)
        #     nums.pop(0)
        #     nums.append(num1*2+num2)
        #     nums.sort()
        #     count+=1
        # return count
        count=0
        heapq.heapify(nums)
        while nums[0]<k:
            num1=heapq.heappop(nums)
            num2=heapq.heappop(nums)
            heapq.heappush(nums,num1*2+num2)
            count+=1
        return count
