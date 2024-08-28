# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        i = 0
        m,n = 0,0
        while i < len(q):
            if i>=n:
                m = i
                n = len(q)
            item = q[i]
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
            i +=1;
        s = 0
        for c in q[m:n]:
            s += c.val
        return s

        