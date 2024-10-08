"""
    Given a string S of lowercase letters, a duplicate removal consists of
    choosing two adjacent and equal letters, and removing them.
    We repeatedly make duplicate removals on S until we no longer can.
    Return the final string after all such duplicate removals have been made.
    It is guaranteed the answer is unique.

    Example:
    Input: "abbaca"
    Output: "ca"
    Explanation:
    For example, in "abbaca" we could remove "bb" since the letters are
    adjacent and equal, and this is the only possible move.  The result of this
    move is that the string is "aaca", of which only "aa" is possible, so the
    final string is "ca".

    Note:
        1. 1 <= S.length <= 20000
        2. S consists only of English lowercase letters.
"""


class solution:
    def removeadajcent(self,s:str) -> str:
        stack=[]
        for letter in s:
            if (len(stack)==0):
                stack.append(letter)
            else:
                if (stack[-1]!=letter):
                    stack.append(letter)
                else:
                    stack.pop()
        return "".join(stack)

sol=solution()
s=input("Enter the string:")
result=sol.removeadajcent(s)
print(result)