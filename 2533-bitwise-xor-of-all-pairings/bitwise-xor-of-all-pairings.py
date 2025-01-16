class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        freq={}
        len1=len(nums1)
        len2=len(nums2)
        for num in nums1:
            freq[num]=freq.get(num,0)+len2
        for num in nums2:
            freq[num]=freq.get(num,0)+len1
        ans=0
        for n in freq:
            if freq[n]&1!=0:
                ans^=n
        return ans


        
