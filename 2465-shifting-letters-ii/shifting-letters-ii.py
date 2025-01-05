class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        cum_shifts = [0 for _ in range(len(s)+1)]
        
        for st, end, d in shifts:
            if d == 0:
                cum_shifts[st] -= 1
                cum_shifts[end+1] += 1
            else:
                cum_shifts[st] += 1
                cum_shifts[end+1] -= 1
        
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += cum_shifts[i]
            
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        return s
        # i=0
        # s=list(s)
        # while i<len(shifts):
        #     start=shifts[i][0]
        #     end=shifts[i][1]
        #     dir=shifts[i][2]
        #     for j in range(start, end+1):
        #         if dir==1 and s[j]=='z':
        #             s[j]='a'
        #         elif dir==1:
        #             s[j]=(chr(ord(s[j])+1))
        #         elif dir==0 and s[j]=='a':
        #             s[j]='z'
        #         else:
        #             s[j]=(chr(ord(s[j])-1))
        #     i+=1
            
        # return ''.join(s)


        