class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i=0
        j=0
        while i<(len(str1)) and j<len(str2):
            if str1[i]==str2[j]:
                #print("str1[i]==str2[j]",str1[i],str2[j])
                i+=1
                j+=1

            elif (ord(str1[i])+1==ord(str2[j])) or (str1[i]=='z' and str2[j]=='a'):
                #print(str1[i],str2[j],"ord(str1[i])+1==ord(str2[j])",ord(str1[i])+1,ord(str2[j]))
                i+=1
                j+=1
            else:
                #print(str1[i])
                i+=1
        
        return True if j==len(str2) else False