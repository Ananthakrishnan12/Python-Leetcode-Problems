"""write a program to remove duplicates in a string"""

class solution:
    def removeduplicates(self,s:str) -> str:
        x=[]
        for i in range(len(s)):
            if s[i] not in x:
                x.append(s[i])
        return x

sol=solution()
s=input("Enter the string:")
result=sol.removeduplicates(s)
for i in range(len(result)):
    print(result[i],end="")