class Solution:
    #def maximumSum(self, nums: List[int]) -> int:
        # i=0
        # out=-1
        # while i<len(nums)-1:
        #     j=i+1
        #     num=nums[i]
        #     sum1=0
        #     rem=0
        #     while(num>0):
        #         rem=num%10
        #         sum1+=rem
        #         num//=10
        #     while(j<len(nums)):
        #         num2=nums[j]
        #         sum2=0
        #         rem=0
        #         while(num2>0):
        #             rem=num2%10
        #             sum2+=rem
        #             num2//=10
                
        #         if sum1==sum2:
        #             #print(sum1,nums[i],nums[j])
        #             out=max(out,(nums[i]+nums[j]))
        #         j+=1
        #     i+=1
        # return out
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums):
        digit_sum_pairs = []

        # Store numbers with their digit sums as pairs
        for number in nums:
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_pairs.append((digit_sum, number))

        # Sort based on digit sums, and if equal, by number value
        digit_sum_pairs.sort()

        max_pair_sum = -1

        # Iterate through the sorted array to find the maximum sum of pairs
        for index in range(1, len(digit_sum_pairs)):
            current_digit_sum = digit_sum_pairs[index][0]
            previous_digit_sum = digit_sum_pairs[index - 1][0]

            # If two consecutive numbers have the same digit sum
            if current_digit_sum == previous_digit_sum:
                current_sum = (
                    digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
                )
                max_pair_sum = max(max_pair_sum, current_sum)

        return max_pair_sum