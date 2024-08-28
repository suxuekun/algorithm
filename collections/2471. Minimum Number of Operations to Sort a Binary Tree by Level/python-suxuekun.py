# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self,m):
        l = [x for x in m]
        h = {l[i]:i for i in range(len(l))}
        m.sort()
        c = 0
        for i in range(len(l)):
            if l[i] != m[i]:
                idx = h[m[i]]
                l[idx],l[i] = l[i],l[idx]
                h[l[idx]] = idx
                h[l[i]] = i
                c +=1
        return c
    
    
    def treetolist(self,root):
        l = [root]
        res = []
        while len(l):
            e = [x.val for x in l]
            res.append(e)
            n = []
            for x in l:
                if x.left:
                    n.append(x.left)
                if x.right:
                    n.append(x.right)
            l = n
        return res
                
        
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        lis = self.treetolist(root)
        c = 0
        for x in lis:
            c += self.count(x)
        return c
        
        
        
        
        