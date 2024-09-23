"""
    Given two binary trees, write a function to check if they are the same or
    not.
    Two binary trees are considered the same if they are structurally identical
    and the nodes have the same value.

    Example 1:
    Input:     1         1
              / \       / \
             2   3     2   3

            [1,2,3],   [1,2,3]
    Output: true

    Example 2:
    Input:     1         1
              /           \
             2             2

            [1,2],     [1,null,2]
    Output: false
"""

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def isSameTree(self,p:TreeNode,q:TreeNode):
        return self.preorder(p,q)
    def preorder(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.preorder(p.left,q.left) and self.preorder(p.right,q.right)

p=TreeNode(1)
p.left=TreeNode(2)
p.right=TreeNode(3)
p.left.left=TreeNode(4)
p.left.right=TreeNode(5)

q=TreeNode(1)
q.left=TreeNode(2)
q.right=TreeNode(3)
q.left.left=TreeNode(4)
q.left.right=TreeNode(6)

sol=Solution()

result=sol.isSameTree(p,q)
print(result)

