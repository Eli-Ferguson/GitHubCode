# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        stack = [ root.left, root.right ]

        while stack :

            nodeL, nodeR = stack.pop(), stack.pop()

            if not nodeL and not nodeR : continue
            elif ( nodeL is None or nodeR is None ) or ( nodeL.val != nodeR.val ) :
                return False
            
            stack.append( nodeL.left )
            stack.append( nodeR.right )
            stack.append( nodeL.right )
            stack.append( nodeR.left )

        return True

# Beats 5.53% Runtime, 54ms
# Beats 5.63% Memory, 16.4mb