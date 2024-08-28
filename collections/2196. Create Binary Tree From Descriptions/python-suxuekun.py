# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:   
        h = {}
        roots={}
        
        for i in descriptions:
            n = i[0]
            parent = h.get(n)
           
            if not parent:
                parent = TreeNode(n)
                h[n] = parent
                roots[n] = parent
                
            child = h.get(i[1])
            if not child:
                child = TreeNode(i[1])
                h[child.val] = child
            if roots.get(child.val):
                del roots[child.val]
            if i[2]:
                parent.left=child
            else:
                parent.right=child

        for i in roots:
            root = roots[i];
        return root
        
        
        
        
            
        
                
                
        
            
                
                
        