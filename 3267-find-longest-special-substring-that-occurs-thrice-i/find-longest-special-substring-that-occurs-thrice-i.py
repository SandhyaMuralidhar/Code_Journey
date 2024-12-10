class Solution:
    def maximumLength(self, s: str) -> int:
        # Create a dictionary to store the count of all substrings.
        count={}
        for i in range (len(s)):
            character_count=0
            character = s[i]
            for j in range(i,len(s)):
                if character==s[j]:
                    character_count+=1
                    count[(character,character_count)]=count.get((character,character_count),0)+1
                else:
                    break
        print(count)    
        ans = 0
        for i in count.items():
            length = i[0][1]
            print(i[0],i[0][1])
            if i[1] >= 3 and length > ans:
                ans = length
        if ans == 0:
            return -1
        return ans