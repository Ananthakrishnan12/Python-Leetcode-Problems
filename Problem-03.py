"""
    Given an array A of strings made only from lowercase letters, return a
    list of all characters that show up in all strings within the list
    (including duplicates).  For example, if a character occurs 3 times in
    all strings but not 4 times, you need to include that character three
    times in the final answer.

    You may return the answer in any order.

    Example:
    Input: ["bella","label","roller"]
    Output: ["e","l","l"]

    Example:
    Input: ["cool","lock","cook"]
    Output: ["c","o"]

    Note:
        1. 1 <= A.length <= 100
        2. 1 <= A[i].length <= 100
        3. A[i][j] is a lowercase letter
"""



class solution:
    def commonchars(self,A:list[str]):
        db={}
        result=[]
        chars=set(A[0])
        for char in chars:
            db[char]=A[0].count(char)
        for word in A[1:]:
            for key in db.keys():
                if key not in word:
                    db[key]=0
                else:
                    db[key]=min(db[key],word.count(key))
        for key,value in db.items():
            result.extend([key]*value)
        return result

input_list=["bella","lella","stella"]

solution=solution()

result=solution.commonchars(input_list)

print(result)
