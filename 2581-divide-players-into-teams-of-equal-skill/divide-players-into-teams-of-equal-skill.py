class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        if n==2:
            return skill[0]*skill[1]
        l=[]
        n=len(skill)
        s=sum(skill)
        teams=n//2
        each_team_sum=s//teams
        while len(skill)!=0:
            ele=skill.pop()
            print(ele)
            if (each_team_sum-ele) in skill:
                skill.remove(each_team_sum-ele)
                l.append((ele,each_team_sum-ele))
            else:
                return -1
        #print(l)
        s=0
        for i,j in l:
            s+=i*j
        return s
        