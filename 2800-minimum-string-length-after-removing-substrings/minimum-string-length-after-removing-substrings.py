class Solution:
    def minLength(self, s: str) -> int:
        # i=0
        # while i<len(s):
        #     print(s[i:i+1])
        #     if s[i:i+2] == 'AB' or s[i:i+2] == 'CD':
        #         s=s[:i]+s[i+2:] 
        #         i=i-1
        #     else:
        #         i=i+1
        # return len(s)

        stack = []
        for char in s:
            if not stack:
                stack.append(char)

            elif char =='B' and stack[-1]=='A':
                stack.pop()

            elif char=='D' and stack[-1]=='C':
                stack.pop()

            else:
                stack.append(char)

        return len(stack)
            

        