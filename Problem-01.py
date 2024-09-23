# https://github.com/YuriSpiridonov/LeetCode

# k=["Apple","Banana","Orange","Pista"]
#
# for i,n in enumerate(k):
#     print(i,n)


"""
Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example:
Input: nums = [3,3], target = 6
Output: [0,1]"""

# class Solution:
#     def twosum(self,nums:list[int],target:int):
#         for i,n in enumerate(nums):
#             if target-n in nums[i+1:]:
#                 return i,i+1+nums[i+1:].index(target-n)
#
# sol=Solution()
# result=sol.twosum([3,5,10,11],21)
#
# print(result)


# Alternative Solution...

class Solution:
    def twosolution(self,nums:list[int],target:int):
        l=len(nums)
        for i in range(l):
            n=nums[i]
            d=target-n
            if d in nums[i+1:]:
                return nums.index(n),i+nums[i+1:].index(d)+1

sol=Solution()
result=sol.twosolution([2,3,4,5],9)
print(result)




