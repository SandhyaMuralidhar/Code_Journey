class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k>0:
            max_ele =max(gifts)
            i=gifts.index(max_ele)
            gifts[i]=floor(gifts[i]**(1/2))
            k-=1
        return sum(gifts)