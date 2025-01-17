class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        l =len(s)
        if l%2==1:
            return False
        unlocked=[]
        open_brackets=[]
        for i in range(l):
            if locked[i]=="0":
                unlocked.append(i)
            elif s[i]=="(":
                open_brackets.append(i)
            elif s[i]==")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
            
        
        while open_brackets and unlocked and open_brackets[-1]<unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()
        if open_brackets:
            return False
        return True
                    


