# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode ) -> bool:
        
        if not root : return True

        def DFS( node, depth ) :
            
            l, r = 0, 0
            
            if node.left :
                l += DFS( node.left, depth+1 )
            
            if node.right :
                r += DFS( node.right, depth+1 )
            
            if l == -1 or r == -1 :
                return -1
            elif abs( l - r ) > 1 :
                return -1
            else :
                return max( l+1, r+1 )


        if DFS( root, 0 ) == -1 : return False
        
        return True

T = TreeNode( 1, None, None )
T.left = TreeNode( 2, None, None )
T.right = TreeNode( 3, None, None )

print( f'Is a Balanced Tree: {Solution.isBalanced( super, T )}' )

# Beats 94.93% Runtime, 240ms
# Beats 23.72% Memory, 18.8mb